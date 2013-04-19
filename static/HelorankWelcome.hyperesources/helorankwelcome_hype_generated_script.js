//	HYPE.documents["HelorankWelcome"]

(function HYPE_DocumentLoader() {
	var resourcesFolderName = "HelorankWelcome.hyperesources";
	var documentName = "HelorankWelcome";
	var documentLoaderFilename = "helorankwelcome_hype_generated_script.js";
	var mainContainerID = "helorankwelcome_hype_container";

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
	
	var resources = {"3":{n:"558661_3006650644567_1738268668_n.jpg",p:1},"1":{n:"Pole-frame1.png",p:1},"4":{n:"Pasted.png",p:1},"2":{n:"Bars.png",p:1},"0":{n:"Pole-frame0.png",p:1}};
	
	var scenes = [{x:0,p:"600px",c:"#FFFFFF",v:{"26":{o:"content-box",h:"3",x:"visible",a:-5,q:"100% 100%",b:-94,j:"absolute",r:"inline",c:1009,k:"div",z:"7",d:516},"3":{o:"content-box",w:"",h:"1",a:38,x:"visible",q:"100% 100%",b:6,j:"absolute",r:"inline",c:100,k:"div",s:"Verdana,Tahoma,Geneva,Sans-Serif",d:400,z:"16",e:"0.000000"},"16":{aU:8,bB:2,G:"#FFFFFF",aV:8,r:"inline",bC:2,e:"0.000000",s:"TrebuchetMS,'Trebuchet MS','Lucida Grande',Tahoma,Arial,Sans-Serif",t:36,Z:"break-word",w:"Tell us what you play.",j:"absolute",x:"visible",aZ:0,k:"div",y:"preserve",z:"19",aS:8,aT:8,a:147,bA:"#7A7A7A",b:252},"11":{o:"content-box",h:"2",x:"visible",a:-110,q:"100% 100%",b:-20,j:"absolute",r:"inline",c:400,k:"div",z:"8",d:400,aY:"0",f:"-90deg"},"14":{aU:8,bB:0,G:"#FFFFFF",aV:8,r:"inline",bC:0,e:"0.000000",s:"Futura,Verdana,sans-serif",t:72,Z:"break-word",v:"normal",w:"Welcome to Helorank ",j:"absolute",x:"visible",aZ:0,k:"div",y:"preserve",z:"20",aS:8,aT:8,a:156,bA:"#000000",b:171},"27":{o:"content-box",h:"4",x:"visible",a:-4,q:"100% 100%",b:-94,j:"absolute",r:"inline",c:108,k:"div",z:"9",d:515},"17":{aU:8,bB:0,G:"#FFFFFF",aV:8,r:"inline",bC:0,e:"0.000000",s:"TrebuchetMS,'Trebuchet MS','Lucida Grande',Tahoma,Arial,Sans-Serif",t:36,Z:"break-word",w:"Tell us who wins.",j:"absolute",x:"visible",aZ:0,k:"div",y:"preserve",z:"18",aS:8,aT:8,a:511,bA:"#000000",b:252},"2":{o:"content-box",h:"0",x:"visible",a:38,q:"100% 100%",b:6,j:"absolute",r:"inline",c:100,k:"div",z:"15",d:400,e:"1.000000"},"18":{aU:8,bB:0,G:"#FFFFFF",aV:8,r:"inline",bC:0,e:"0.000000",s:"TrebuchetMS,'Trebuchet MS','Lucida Grande',Tahoma,Arial,Sans-Serif",t:36,Z:"break-word",w:"We'll set the record straight.",j:"absolute",x:"visible",aZ:0,k:"div",y:"preserve",z:"17",aS:8,aT:8,a:158,bA:"#000000",b:292}},n:"Untitled Scene",T:{kTimelineDefaultIdentifier:{d:4.07,i:"kTimelineDefaultIdentifier",n:"Main Timeline",a:[{f:"2",t:0,d:0.15,i:"e",e:"0.900213",s:"0.000000",o:"3"},{f:"2",t:0,d:0.15,i:"e",e:"1.000000",s:"0.000000",o:"14"},{f:"2",t:0,d:0.15,i:"bC",e:0,s:2,o:"16"},{f:"2",t:0,d:0.15,i:"bB",e:1,s:2,o:"16"},{f:"2",t:0.15,d:0.15,i:"e",e:"0.000000",s:"0.900213",o:"3"},{f:"2",t:1,d:0,i:"e",e:"0.000000",s:"0.000000",o:"3"},{f:"2",t:1,d:0.15,i:"e",e:"0.896635",s:"0.000000",o:"3"},{f:"2",t:1.15,d:0.15,i:"e",e:"0.000000",s:"0.896635",o:"3"},{f:"2",t:1.22,d:1,i:"f",e:"0deg",s:"-90deg",o:"11"},{f:"2",t:2,d:0.15,i:"e",e:"1.000000",s:"0.000000",o:"3"},{f:"2",t:2.22,d:0.15,i:"a",e:164,s:147,o:"16"},{f:"2",t:2.22,d:0.15,i:"e",e:"1.000000",s:"0.000000",o:"16"},{f:"2",t:3.07,d:0.15,i:"e",e:"1.000000",s:"0.000000",o:"17"},{f:"2",t:3.07,d:0.15,i:"a",e:528,s:511,o:"17"},{f:"2",t:3.22,d:0.15,i:"a",e:166,s:158,o:"18"},{f:"2",t:3.22,d:0.15,i:"e",e:"1.000000",s:"0.000000",o:"18"}],f:30}},o:"1"}];
	
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

