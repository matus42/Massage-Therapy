document.addEventListener("DOMContentLoaded", function() {
    const dateField = document.querySelector("input[name='date']");
    const timeSlotField = document.querySelector("select[name='time_slot']");
    const today = new Date().toISOString().split('T')[0];

    dateField.setAttribute('min', today);

    function updateTimeSlots() {
        const selectedDate = dateField.value;
        const currentDate = new Date();
        const currentHour = currentDate.getHours();

        fetch(`/booking/get_available_time_slots/?date=${selectedDate}`)
            .then(response => response.json())
            .then(data => {
                timeSlotField.innerHTML = ''; // Clear existing options

                if (data.message && data.message === 'Fully booked') {
                    addOption('This day is fully booked.', '');
                } else {
                    data.available_slots.forEach(slot => {
                        // If selectedDate is today, filter out past time slots
                        if (selectedDate === today && !isTimeSlotInFuture(slot[0], currentHour)) {
                            return; // Skip adding this time slot
                        }
                        addOption(slot[1], slot[0]); // Slot text for display, value for backend
                    });
                }
            })
            .catch(error => {
                console.error('Error fetching time slots:', error);
                addOption('Error loading time slots', '');
            });
    }

    function addOption(text, value) {
        const optionElement = document.createElement("option");
        optionElement.text = text;
        optionElement.value = value;
        timeSlotField.appendChild(optionElement);
    }

    function isTimeSlotInFuture(slot, currentHour) {
        const slotHour = parseInt(slot);
        return slotHour > currentHour;
    }

    dateField.addEventListener("change", updateTimeSlots);
});
