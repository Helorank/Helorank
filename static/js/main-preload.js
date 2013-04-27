/* ONLY resources that must be loaded upfront */

/* Facebook functions */
function login() {
  console.log("ello!");
    FB.login(function(response) {
      if (response.authResponse) {
          testAPI();
      } else {
           console.log("Facebook login cancelled");
      }
  });
  }

  function testAPI() {
    console.log('Welcome!  Fetching your information.... ');
    FB.api('/me', function(response) {
        console.log('Good to see you, ' + response.name + '.');
    });
}