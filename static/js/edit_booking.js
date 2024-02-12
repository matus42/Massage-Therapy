document.addEventListener("DOMContentLoaded", function() {
    const dateField = document.querySelector("input[name='date']");
    const today = new Date().toISOString().split('T')[0]; // Get today's date in the required format
    dateField.setAttribute('min', today); // Set the minimum date to today, preventing past dates from being selected

    const timeSlotField = document.querySelector("select[name='time_slot']");
    const currentBookingTimeSlot = timeSlotField.value; // Store the current booking time slot, if any

    function updateTimeSlots() {
        const selectedDate = dateField.value;
        const currentDate = new Date();
        const currentHour = currentDate.getHours();

        fetch(`/booking/get_available_time_slots/?date=${selectedDate}`)
            .then(response => response.json())
            .then(data => {
                timeSlotField.innerHTML = ''; // Clear existing options

                data.available_slots.forEach(slot => {
                    // If selectedDate is today, filter out past time slots
                    if (!(selectedDate === today && !isTimeSlotInFuture(slot[0], currentHour))) {
                        const optionElement = document.createElement("option");
                        optionElement.value = slot[0]; // Slot value for backend processing
                        optionElement.text = slot[1]; // Slot text for display to the user
                        timeSlotField.appendChild(optionElement);
                    }
                });

                // Add the current booking time slot if it's not included and is valid
                if (!data.available_slots.some(slot => slot[0] === currentBookingTimeSlot) &&
                    (selectedDate !== today || isTimeSlotInFuture(currentBookingTimeSlot, currentHour))) {
                    const optionElement = document.createElement("option");
                    optionElement.value = currentBookingTimeSlot;
                    optionElement.text = `Current Booking: ${currentBookingTimeSlot}`;
                    optionElement.selected = true;
                    timeSlotField.appendChild(optionElement);
                }
            })
            .catch(error => {
                console.error('Error fetching time slots:', error);
                // Handle error, maybe by showing an error message or logging
                timeSlotField.innerHTML = '';
                const optionElement = document.createElement("option");
                optionElement.value = '';
                optionElement.text = 'Error loading time slots';
                timeSlotField.appendChild(optionElement);
            });
    }

    function isTimeSlotInFuture(slot, currentHour) {
        const slotHour = parseInt(slot);
        return slotHour > currentHour;
    }

    dateField.addEventListener("change", updateTimeSlots);
    updateTimeSlots(); 
});
