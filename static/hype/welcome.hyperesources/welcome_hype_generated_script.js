//	HYPE.documents["welcome"]

(function HYPE_DocumentLoader() {
	var resourcesFolderName = "static/hype/welcome.hyperesources";
	var documentName = "welcome";
	var documentLoaderFilename = "welcome_hype_generated_script.js";
	var mainContainerID = "welcome_hype_container";

	// find the URL for this script's absolute path and set as the resourceFolderName
	try {
		var scripts = document.getElementsByTagName('script');
		for(var i = 0; i < scripts.length; i++) {
			var scriptSrc = scripts[i].src;
			if(scriptSrc != null && scriptSrc.indexOf(documentLoaderFilename) != -1) {
				resourcesFolderName = scriptSrc.substr(0, scriptSrc.lastIndexOf("/"));
				break;
			}
		}
	} catch(err) {	}

	// Legacy support
	if (typeof window.HYPE_DocumentsToLoad == "undefined") {
		window.HYPE_DocumentsToLoad = new Array();
	}
 
	// load HYPE.js if it hasn't been loaded yet
	if(typeof HYPE_160 == "undefined") {
		if(typeof window.HYPE_160_DocumentsToLoad == "undefined") {
			window.HYPE_160_DocumentsToLoad = new Array();
			window.HYPE_160_DocumentsToLoad.push(HYPE_DocumentLoader);

			var headElement = document.getElementsByTagName('head')[0];
			var scriptElement = document.createElement('script');
			scriptElement.type= 'text/javascript';
			scriptElement.src = resourcesFolderName + '/' + 'HYPE.js?hype_version=160';
			headElement.appendChild(scriptElement);
		} else {
			window.HYPE_160_DocumentsToLoad.push(HYPE_DocumentLoader);
		}
		return;
	}
	
	// handle attempting to load multiple times
	if(HYPE.documents[documentName] != null) {
		var index = 1;
		var originalDocumentName = documentName;
		do {
			documentName = "" + originalDocumentName + "-" + (index++);
		} while(HYPE.documents[documentName] != null);
		
		var allDivs = document.getElementsByTagName("div");
		var foundEligibleContainer = false;
		for(var i = 0; i < allDivs.length; i++) {
			if(allDivs[i].id == mainContainerID && allDivs[i].getAttribute("HYPE_documentName") == null) {
				var index = 1;
				var originalMainContainerID = mainContainerID;
				do {
					mainContainerID = "" + originalMainContainerID + "-" + (index++);
				} while(document.getElementById(mainContainerID) != null);
				
				allDivs[i].id = mainContainerID;
				foundEligibleContainer = true;
				break;
			}
		}
		
		if(foundEligibleContainer == false) {
			return;
		}
	}
	
	var hypeDoc = new HYPE_160();
	
	var attributeTransformerMapping = {b:"i",c:"i",bC:"i",d:"i",aS:"i",M:"i",e:"f",aT:"i",N:"i",f:"d",O:"i",g:"c",aU:"i",P:"i",Q:"i",aV:"i",R:"c",bG:"f",aW:"f",aI:"i",S:"i",bH:"d",l:"d",aX:"i",T:"i",m:"c",bI:"f",aJ:"i",n:"c",aK:"i",bJ:"f",X:"i",aL:"i",A:"c",aZ:"i",Y:"bM",B:"c",bK:"f",bL:"f",C:"c",D:"c",t:"i",E:"i",G:"c",bA:"c",a:"i",bB:"i"};
	
	var resources = {"0":{n:"frame0.png",p:1},"1":{n:"frame3.png",p:1},"2":{n:"frame4.png",p:1}};
	
	var scenes = [{x:0,p:"600px",c:"#333333",v:{"3":{o:"content-box",h:"1",aI:0,x:"visible",q:"100% 100%",a:0,j:"absolute",r:"inline",c:1170,k:"div",z:"2",d:200,b:0,aK:0,e:"0.000000",aJ:0,aL:0},"6":{aV:8,w:"<p style=\"font-family: 'Montserrat', sans-serif;\">Track every game you play.</p>",a:495,x:"visible",Z:"break-word",y:"preserve",j:"absolute",r:"inline",z:"5",k:"div",b:52,aT:8,aS:8,t:28,e:"0.000000",aU:8,G:"#999999"},"4":{o:"content-box",h:"2",aI:0,x:"visible",q:"100% 100%",a:0,j:"absolute",r:"inline",c:1170,k:"div",z:"3",d:200,b:0,aK:0,e:"0.000000",aJ:0,aL:0},"2":{o:"content-box",w:"",h:"0",aI:0,x:"visible",q:"100% 100%",a:0,j:"absolute",r:"inline",c:1170,k:"div",z:"1",d:200,b:0,t:15,aK:0,aJ:0,aL:0},"7":{aV:8,w:"<p style=\"font-family: 'Montserrat', sans-serif;\">Create power rankings among your friends.</p>",a:495,x:"visible",Z:"break-word",y:"preserve",j:"absolute",r:"inline",z:"4",k:"div",b:89,aT:8,aS:8,t:28,e:"0.000000",aU:8,G:"#999999"},"5":{aV:8,w:"<p style=\"font-family: 'Montserrat', sans-serif;\">Welcome to Helorank</p>",a:483,x:"visible",Z:"break-word",y:"preserve",j:"absolute",r:"inline",c:623,k:"div",z:"6",aT:8,d:116,t:52,e:"0.000000",b:-32,aU:8,G:"#99CC99",aS:8}},n:"Untitled Scene",T:{kTimelineDefaultIdentifier:{d:5.03,i:"kTimelineDefaultIdentifier",n:"Main Timeline",a:[{f:"2",t:0,d:0.15,i:"e",e:"0.806900",s:"0.000000",o:"3"},{f:"2",t:0.15,d:0.15,i:"e",e:"0.000000",s:"0.806900",o:"3"},{f:"2",t:1,d:0.15,i:"e",e:"0.798760",s:"0.000000",o:"3"},{f:"2",t:1.15,d:0.15,i:"e",e:"0.000000",s:"0.798760",o:"3"},{f:"2",t:2,d:1,i:"e",e:"1.000000",s:"0.000000",o:"4"},{f:"2",t:3,d:0.21,i:"a",e:519,s:483,o:"5"},{f:"2",t:3,d:0.21,i:"e",e:"1.000000",s:"0.000000",o:"5"},{f:"2",t:3.21,d:0.21,i:"a",e:531,s:495,o:"6"},{f:"2",t:3.21,d:0.21,i:"e",e:"1.000000",s:"0.000000",o:"6"},{f:"2",t:4.12,d:0.21,i:"e",e:"1.000000",s:"0.000000",o:"7"},{f:"2",t:4.12,d:0.21,i:"a",e:531,s:495,o:"7"}],f:30}},o:"1"}];
	
	var javascripts = [];
	
	var functions = {};
	var javascriptMapping = {};
	for(var i = 0; i < javascripts.length; i++) {
		try {
			javascriptMapping[javascripts[i].identifier] = javascripts[i].name;
			eval("functions." + javascripts[i].name + " = " + javascripts[i].source);
		} catch (e) {
			hypeDoc.log(e);
			functions[javascripts[i].name] = (function () {});
		}
	}
	
	hypeDoc.setAttributeTransformerMapping(attributeTransformerMapping);
	hypeDoc.setResources(resources);
	hypeDoc.setScenes(scenes);
	hypeDoc.setJavascriptMapping(javascriptMapping);
	hypeDoc.functions = functions;
	hypeDoc.setCurrentSceneIndex(0);
	hypeDoc.setMainContentContainerID(mainContainerID);
	hypeDoc.setResourcesFolderName(resourcesFolderName);
	hypeDoc.setShowHypeBuiltWatermark(0);
	hypeDoc.setShowLoadingPage(false);
	hypeDoc.setDrawSceneBackgrounds(true);
	hypeDoc.setGraphicsAcceleration(true);
	hypeDoc.setDocumentName(documentName);

	HYPE.documents[documentName] = hypeDoc.API;
	document.getElementById(mainContainerID).setAttribute("HYPE_documentName", documentName);

	hypeDoc.documentLoad(this.body);
}());

