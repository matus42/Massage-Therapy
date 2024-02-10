document.addEventListener("DOMContentLoaded", function() {
    const dateField = document.querySelector("input[name='date']");
    const timeSlotField = document.querySelector("select[name='time_slot']");
    const currentBookingTimeSlot = timeSlotField.value; // Store the current booking time slot

    function updateTimeSlots() {
        const selectedDate = dateField.value;
        fetch(`/booking/get_available_time_slots/?date=${selectedDate}`)
            .then(response => response.json())
            .then(data => {
                timeSlotField.innerHTML = ''; // Clear existing options

                // Populate with available time slots
                data.available_slots.forEach(slot => {
                    const optionElement = document.createElement("option");
                    optionElement.value = slot[0]; // The value to submit with the form
                    optionElement.text = slot[1]; // The text to show the user
                    timeSlotField.appendChild(optionElement);
                });

                // Add the current booking time slot if it's not included
                if (!data.available_slots.some(slot => slot[0] === currentBookingTimeSlot)) {
                    const optionElement = document.createElement("option");
                    optionElement.value = currentBookingTimeSlot;
                    optionElement.text = `Current Booking : ${currentBookingTimeSlot}`;
                    optionElement.selected = true; // Mark this option as selected
                    timeSlotField.appendChild(optionElement);
                }
            })
            .catch(error => {
                console.error('Error fetching time slots:', error);
                // Handle errors, maybe clear the dropdown and show an error message
                timeSlotField.innerHTML = '';
                const optionElement = document.createElement("option");
                optionElement.value = '';
                optionElement.text = 'Error loading time slots';
                timeSlotField.appendChild(optionElement);
            });
    }

    dateField.addEventListener("change", updateTimeSlots);
    updateTimeSlots(); 
});
