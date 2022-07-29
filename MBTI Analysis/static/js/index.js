$(document).ready(function(){
    // Add smooth scrolling to all links
    $("a").on('click', function(event) {

        // Make sure this.hash has a value before overriding default behavior
        if (this.hash !== "") {
            // Prevent default anchor click behavior
            event.preventDefault();

            // Store hash
            var hash = this.hash;

            // Using jQuery's animate() method to add smooth page scroll
            // 400 is speed of scroll in milliseconds
            $('html, body').animate({
                scrollTop: $(hash).offset().top - 50 //50 is offset from top of page
            }, 400, function(){

                //scroll to page
                window.scrollTo(window.scrollX, window.scrollY);
            });
        } // End if
    });
});

// Navbar close when outide of navbar is clicked
$(document).click(function(e) {
    if (!$(e.target).is('a')) {
        $('.collapse').collapse("hide");
    }
});

// Navbar close when link is clicked
$('.nav-link').click(function(){
    $('.collapse').collapse("hide");
});
