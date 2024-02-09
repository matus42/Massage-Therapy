document.addEventListener("DOMContentLoaded", function() {
    const dateField = document.querySelector("input[name='date']");
    const timeSlotField = document.querySelector("select[name='time_slot']");
    const today = new Date().toISOString().split('T')[0];
    dateField.setAttribute('min', today);

    function updateTimeSlots() {
        const selectedDate = dateField.value;
        fetch(`/booking/get_available_time_slots/?date=${selectedDate}`)
            .then(response => response.json())
            .then(data => {
                timeSlotField.innerHTML = ''; // Clear existing options

                // Check if there's a message indicating that no slots are available
                if (data.message && data.message === 'Fully booked') {
                    // If fully booked, display an option indicating so
                    const optionElement = document.createElement("option");
                    optionElement.value = ''; // No specific value
                    optionElement.text = 'This day is fully booked.'; // Informative text for the user
                    timeSlotField.appendChild(optionElement);
                } else {
                    // If slots are available, populate the dropdown with them
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
                // Optionally, handle errors by clearing the dropdown and showing an error message
                timeSlotField.innerHTML = '';
                const optionElement = document.createElement("option");
                optionElement.value = '';
                optionElement.text = 'Error loading time slots';
                timeSlotField.appendChild(optionElement);
            });
    }

    dateField.addEventListener("change", updateTimeSlots);
});
