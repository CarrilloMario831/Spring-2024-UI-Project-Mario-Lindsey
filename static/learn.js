$(document).ready(function() {

    // Group hover for Nayarit and Sinaloa
    $('#MX-NAY, #MX-SIN').hover(
        function() {
        // Mouse enter
        $('#MX-NAY, #MX-SIN').css('fill', '#006847'); // Change fill to red
        
        }, 
        function() {
        // Mouse leave
        $('#MX-NAY, #MX-SIN').css('fill', '#8ebd99'); // Change fill back to default
        }
    );

    // Group hover for Jalisco, Colima, Zacatecas, Michoacán, Guanajuato, Aguascalientes
    $('#MX-JAL, #MX-COL, #MX-ZAC, #MX-MIC, #MX-GUA, #MX-AGU').hover(
        function() {
        // Mouse enter
        $('#MX-JAL, #MX-COL, #MX-ZAC, #MX-MIC, #MX-GUA, #MX-AGU').css('fill', '#006847'); // Change fill to red
        },
        function() {
        // Mouse leave
        $('#MX-JAL, #MX-COL, #MX-ZAC, #MX-MIC, #MX-GUA, #MX-AGU').css('fill', '#8ebd99'); // Change fill back to default
        }
    );

    // Group hover for Nuevo León, Chihuahua, Coahuila, Durango, Tamaulipas, Sonora, Baja California, Baja California Sur
    $('#MX-NEL, #MX-CHH, #MX-COA, #MX-DUR, #MX-TAM, #MX-SON, #MX-BCN, #MX-BCS').hover(
        function() {
        // Mouse enter
        $('#MX-NEL, #MX-CHH, #MX-COA, #MX-DUR, #MX-TAM, #MX-SON, #MX-BCN, #MX-BCS').css('fill', '#006847'); // Change fill to red
        },
        function() {
        // Mouse leave
        $('#MX-NEL, #MX-CHH, #MX-COA, #MX-DUR, #MX-TAM, #MX-SON, #MX-BCN, #MX-BCS').css('fill', '#8ebd99'); // Change fill back to default
        }
    );

    // Group hover for Veracruz, Campeche, Tabasco, Hidalgo, San Luis Potosí, Querétaro, Tlaxcala, Chiapas, Quintana Roo, Yucatán
    $('#MX-VER, #MX-CAM, #MX-TAB, #MX-HID, #MX-SLP, #MX-QUE, #MX-TLA, #MX-CHP, #MX-ROO, #MX-YUC').hover(
        function() {
        // Mouse enter
        $('#MX-VER, #MX-CAM, #MX-TAB, #MX-HID, #MX-SLP, #MX-QUE, #MX-TLA, #MX-CHP, #MX-ROO, #MX-YUC').css('fill', '#006847'); // Change fill to red
        },
        function() {
        // Mouse leave
        $('#MX-VER, #MX-CAM, #MX-TAB, #MX-HID, #MX-SLP, #MX-QUE, #MX-TLA, #MX-CHP, #MX-ROO, #MX-YUC').css('fill', '#8ebd99'); // Change fill back to default
        }
    );

    $('#MX-MEX, #MX-DIF, #MX-PUE, #MX-MOR').hover(
        function() {
            $('#MX-MEX, #MX-DIF, #MX-PUE, #MX-MOR').css('fill', '#006847');
        },
        function() {
            $('#MX-MEX, #MX-DIF, #MX-PUE, #MX-MOR').css('fill', '#8ebd99');
        }
    );

    $('#MX-GRO, #MX-OAX').hover(
        function() {
            $('#MX-GRO, #MX-OAX').css('fill', '#006847');
        },
        function() {
            $('#MX-GRO, #MX-OAX').css('fill', '#8ebd99');
        }
    );

    // Click events to navigate to different pages based on region
    $('#MX-NAY, #MX-SIN').click(function() {
        window.location.href = '/learn/2'; // Example URL for the Nayarit and Sinaloa region
    });

    $('#MX-JAL, #MX-COL, #MX-ZAC, #MX-MIC, #MX-GUA, #MX-AGU').click(function() {
        window.location.href = '/learn/3'; // Adjust URL as necessary
    });

    $('#MX-NEL, #MX-CHH, #MX-COA, #MX-DUR, #MX-TAM, #MX-SON, #MX-BCN, #MX-BCS').click(function() {
        window.location.href = '/learn/4'; // Adjust URL as necessary
    });

    $('#MX-VER, #MX-CAM, #MX-TAB, #MX-HID, #MX-SLP, #MX-QUE, #MX-TLA, #MX-CHP, #MX-ROO, #MX-YUC').click(function() {
        window.location.href = '/learn/5'; // Adjust URL as necessary
    });

    $('#MX-MEX, #MX-DIF, #MX-PUE, #MX-MOR').click(function() {
        window.location.href = '/learn/6'; // Adjust URL as necessary
    });

    $('#MX-GRO, #MX-OAX').click(function() {
        window.location.href = '/learn/7'; // Adjust URL as necessary
    });

    
    
    
});
