
/* Hype functions */
function scaleSite()
	    {
	      containerw = $("#containingElement").width();
	      containerh = $("#containingElement").height();
	      sitew = $('#scalecontainer').width();
	      siteh = $('#scalecontainer').height();
	      f = containerw/sitew;
	      f = containerh/siteh<f?containerh/siteh:f;
	      if(!alsoenlarge && f>1) f = 1;
	      $('#scalecontainer').css({
	        "-moz-transform"    : "scale("+f+")",
	        "-webkit-transform" : "scale("+f+")",
	        "-ms-transform"     : "scale("+f+")",
	        "-o-transform"      : "scale("+f+")",
	        "transform"         : "scale("+f+")",
	        "center"              : ((containerw-(sitew*f))/2)+"px",
	      });
	    }
function isScalePossible()
{
  can = 'MozTransform' in document.body.style;
  if(!can) can = 'webkitTransform' in document.body.style;
  if(!can) can = 'msTransform' in document.body.style;
  if(!can) can = 'OTransform' in document.body.style;
  if(!can) can = 'transform' in document.body.style;
  if(!can) can = 'Transform' in document.body.style;
  return can;
}
