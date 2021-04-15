// Category slider starts
var elem = document.querySelector('.product__categories');
var flkty = new Flickity(elem, {
    // options
    cellAlign: 'left',
    wrapAround: true,
});

// element argument can be a selector string
//   for an individual element
var flkty = new Flickity('.product__categories', {
    // options
});

// Category slider ends


// Showing content of category slider starts

var catTitle = document.getElementsByClassName("cat__button");
const itemBox = document.getElementsByClassName("itembox");

// Hide those product which are index 7, or greater than index 7
for (let i = 0; i < itemBox.length; i++) {
    if (i >= 6) {
        itemBox[i].style.display = "none";
    }
}

for (let i = 0; i < catTitle.length; i++) {
    catTitle[i].addEventListener("click", function() {
        const value = catTitle[i].getAttribute("data-filter");
        // console.log(value);

        const catValue = catTitle[i];

        for (let i = 0; i < catTitle.length; i++) {
            if (catTitle[i] === catValue) {
                catValue.classList.add("activeProd");
            } else {
                catTitle[i].classList.remove("activeProd");
            }
        }

        if (value === "all") {
            $(".itembox").show("1000");
            const itemBox = document.getElementsByClassName("itembox");

            // Hide those product which are index 7, or greater than index 7
            for (let i = 0; i < itemBox.length; i++) {
                if (i >= 6) {
                    itemBox[i].style.display = "none";
                }
            }
        } else {
            $(".itembox").not("." + value).hide("1000");
            $(".itembox").filter("." + value).show("1000");
            const itemBox = document.getElementsByClassName("itembox");

            // Hide those product which are index 7, or greater than index 7
            for (let i = 0; i < itemBox.length; i++) {
                if (i >= 6) {
                    itemBox[i].style.display = "none";
                }
            }
        }
    });
}

// Showing content of category slider ends


// Category slider starts
var elem = document.querySelector('.brands');
var flkty = new Flickity(elem, {
    // options
    cellAlign: 'left',
    wrapAround: true,
});

// element argument can be a selector string
//   for an individual element
var flkty = new Flickity('.brands', {
    // options
});

// Category slider ends