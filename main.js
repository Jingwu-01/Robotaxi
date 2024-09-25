window.onload = function() {
    const fixedRateRadio = document.getElementById("electricityRateFixed");
    const variableRateRadio = document.getElementById("electricityRateVariable");
    const electricityPriceDiv = document.getElementById("electricityPriceDiv");

    function toggleElectricityPrice() {
        if (fixedRateRadio.checked) {
          electricityPriceDiv.style.display = "block";
        } else {
          electricityPriceDiv.style.display = "none";
        }
      }
  
    fixedRateRadio.addEventListener("change", toggleElectricityPrice);
    variableRateRadio.addEventListener("change", toggleElectricityPrice);
  
    toggleElectricityPrice();
  };
  