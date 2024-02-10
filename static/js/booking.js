document.addEventListener("DOMContentLoaded", function() {
    const dateField = document.querySelector("input[name='date']");
    const timeSlotField = document.querySelector("select[name='time_slot']");
    const today = new Date().toISOString().split('T')[0];
    dateField.setAttribute('min', today);

    // Function to fetch and update time slots based on the selected date
    function updateTimeSlots() {
        const selectedDate = dateField.value;

        if (selectedDate) { // Only proceed if a date has been selected
            fetch(`/booking/get_available_time_slots/?date=${selectedDate}`)
                .then(response => response.json())
                .then(data => {
                    timeSlotField.innerHTML = ''; // Clear existing options

                    if (data.message && data.message === 'Fully booked') {
                        const optionElement = document.createElement("option");
                        optionElement.value = ''; // No specific value
                        optionElement.text = 'This day is fully booked.'; // Informative text for the user
                        timeSlotField.appendChild(optionElement);
                    } else {
                        data.available_slots.forEach(slot => {
                            const optionElement = document.createElement("option");
                            optionElement.value = slot[0]; // Slot value for backend processing
                            optionElement.text = slot[1]; // Slot text for display to the user
                            timeSlotField.appendChild(optionElement);
                        });
                    }
                })
                .catch(error => {
                    console.error('Error fetching time slots:', error);
                    timeSlotField.innerHTML = '';
                    const optionElement = document.createElement("option");
                    optionElement.value = '';
                    optionElement.text = 'Error loading time slots';
                    timeSlotField.appendChild(optionElement);
                });
        } else {
            timeSlotField.innerHTML = ''; // Clear existing options
            const optionElement = document.createElement("option");
            optionElement.value = '';
            optionElement.text = 'Please select a date'; // Prompt to select a date
            timeSlotField.appendChild(optionElement);
        }
    }

    // Call updateTimeSlots function when the date field value changes
    dateField.addEventListener("change", updateTimeSlots);

});
