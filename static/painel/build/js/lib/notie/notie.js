var notie=function(){function e(){$=document.body.style.height,_=document.body.style.overflow,document.body.style.height="100%",document.body.style.overflow="hidden"}function t(){document.body.style.height=$,document.body.style.overflow=_}function n(e,t,n){document.activeElement.blur(),se++,setTimeout(function(){se--},1e3*h+10),1==se&&(le?(clearTimeout(ie),clearTimeout(oe),o(function(){i(e,t,n)})):i(e,t,n))}function i(e,t,n){le=!0;var i=0;if("undefined"==typeof n)var i=3e3;else i=n<1?1e3:1e3*n;switch(e){case 1:ee.style.backgroundColor=b;break;case 2:ee.style.backgroundColor=v;break;case 3:ee.style.backgroundColor=w;break;case 4:ee.style.backgroundColor=x}ne.innerHTML=t,ee.style.top="-10000px",ee.style.display="table",ee.style.top="-"+ee.offsetHeight-5+"px",ie=setTimeout(function(){c&&(ee.style.boxShadow="none"),ee.style.MozTransition="all "+h+"s ease",ee.style.WebkitTransition="all "+h+"s ease",ee.style.transition="all "+h+"s ease",ee.style.top=0,oe=setTimeout(function(){o(function(){})},i)},20)}function o(e){ee.style.top="-"+ee.offsetHeight-5+"px",setTimeout(function(){c&&(ee.style.boxShadow=""),ee.style.MozTransition="",ee.style.WebkitTransition="",ee.style.transition="",ee.style.top="-10000px",le=!1,e&&e()},1e3*h+10)}function l(e,t,n,i){document.activeElement.blur(),le?(clearTimeout(ie),clearTimeout(oe),o(function(){s(e,t,n,i)})):s(e,t,n,i)}function s(t,n,i,o){function l(){ue.innerHTML=t,pe.innerHTML=n,fe.innerHTML=i,de.style.top="-10000px",de.style.display="table",de.style.top="-"+de.offsetHeight-5+"px",ae.style.display="block",setTimeout(function(){c&&(de.style.boxShadow="none"),de.style.MozTransition="all "+h+"s ease",de.style.WebkitTransition="all "+h+"s ease",de.style.transition="all "+h+"s ease",de.style.top=0,ae.style.opacity="0.75",setTimeout(function(){he=!0},1e3*h+10)},20)}e(),re.onclick=function(){d(),setTimeout(function(){o()},1e3*h+10)},he?(d(),setTimeout(function(){l()},1e3*h+10)):l()}function d(){de.style.top="-"+de.offsetHeight-5+"px",ae.style.opacity="0",setTimeout(function(){c&&(de.style.boxShadow=""),de.style.MozTransition="",de.style.WebkitTransition="",de.style.transition="",ae.style.display="none",de.style.top="-10000px",t(),he=!1},1e3*h+10)}function a(e,t,n,i,l,s,d){document.activeElement.blur(),setTimeout(function(){xe.focus()},1e3*h),xe.setAttribute("type",i),xe.setAttribute("placeholder",l),xe.value="","undefined"!=typeof d&&d.length>0&&(xe.value=d),le?(clearTimeout(ie),clearTimeout(oe),o(function(){y(e,t,n,s)})):y(e,t,n,s)}function y(t,n,i,o){function l(){ke.innerHTML=t,ze.innerHTML=n,Ee.innerHTML=i,me.style.top="-10000px",me.style.display="table",me.style.top="-"+me.offsetHeight-5+"px",be.style.display="block",setTimeout(function(){c&&(me.style.boxShadow=""),me.style.MozTransition="all "+h+"s ease",me.style.WebkitTransition="all "+h+"s ease",me.style.transition="all "+h+"s ease",me.style.top=0,be.style.opacity="0.75",setTimeout(function(){Ce=!0},1e3*h+10)},20)}e(),ge.onclick=function(){r(),setTimeout(function(){o(xe.value)},1e3*h+10)},Ce?(r(),setTimeout(function(){l()},1e3*h+10)):l()}function r(){me.style.top="-"+me.offsetHeight-5+"px",be.style.opacity="0",setTimeout(function(){c&&(me.style.boxShadow=""),me.style.MozTransition="",me.style.WebkitTransition="",me.style.transition="",be.style.display="none",me.style.top="-10000px",t(),Ce=!1},1e3*h+10)}var c=!0,u="1rem",p="1rem",f=600,h=.3,m=!0,b="#46c35f",v="#f29824",w="#fa424a",x="#ac6bec",g="#FFF",T="#00a8ff",k="#46c35f",z="#fa424a",E="#FFF",C="#FFF",S="#FFF",W="notie-alert-outer",F="notie-alert-inner",L="notie-alert-text",M="notie-confirm-outer",H="notie-confirm-inner",A="notie-confirm-background",I="notie-confirm-yes",R="notie-confirm-no",j="notie-confirm-text",q="notie-confirm-yes-text",B="notie-confirm-no-text",D="notie-input-outer",G="notie-input-inner",J="notie-input-background",K="notie-input-div",N="notie-input-field",O="notie-input-yes",P="notie-input-no",Q="notie-input-text",U="notie-input-yes-text",V="notie-input-no-text",X=function(e){window.innerWidth<=f?e.style.fontSize=u:e.style.fontSize=p},Y=500,Z=function(e,t,n){var i;return function(){var o=this,l=arguments,s=function(){i=null,n||e.apply(o,l)},d=n&&!i;clearTimeout(i),i=setTimeout(s,t),d&&e.apply(o,l)}};window.addEventListener("keydown",function(e){var t=13==e.which||13==e.keyCode,n=27==e.which||27==e.keyCode;le?(t||n)&&(clearTimeout(ie),clearTimeout(oe),o()):he?t?re.click():n&&ce.click():Ce&&(t?ge.click():n&&Te.click())}),"undefined"==typeof Element.prototype.addEventListener&&(Element.prototype.addEventListener=Window.prototype.addEventListener=function(e,t){return e="on"+e,this.attachEvent(e,t)});var $,_,ee=document.createElement("div");ee.id=W,ee.style.position="fixed",ee.style.top="0",ee.style.left="0",ee.style.zIndex="999999999",ee.style.height="auto",ee.style.width="100%",ee.style.display="none",ee.style.textAlign="center",ee.style.cursor="default",ee.style.MozTransition="",ee.style.WebkitTransition="",ee.style.transition="",ee.style.cursor="pointer",ee.onclick=function(){clearTimeout(ie),clearTimeout(oe),o()};var te=document.createElement("div");te.id=F,te.style.padding="15px",te.style.display="table-cell",te.style.verticalAlign="middle",ee.appendChild(te);var ne=document.createElement("span");ne.id=L,ne.style.color=g,ne.style.fontWeight="600",window.innerWidth<=f?ne.style.fontSize=u:ne.style.fontSize=p,window.addEventListener("resize",Z(X.bind(null,ne),Y),!0),te.appendChild(ne),document.body.appendChild(ee);var ie,oe,le=!1,se=0,de=document.createElement("div");de.id=M,de.style.position="fixed",de.style.top="0",de.style.left="0",de.style.zIndex="999999998",de.style.height="auto",de.style.width="100%",de.style.display="none",de.style.textAlign="center",de.style.MozTransition="",de.style.WebkitTransition="",de.style.transition="";var ae=document.createElement("div");ae.id=A,ae.style.position="fixed",ae.style.top="0",ae.style.left="0",ae.style.zIndex="999999997",ae.style.height="100%",ae.style.width="100%",ae.style.display="none",ae.style.backgroundColor="white",ae.style.MozTransition="all "+h+"s ease",ae.style.WebkitTransition="all "+h+"s ease",ae.style.transition="all "+h+"s ease",ae.style.opacity="0",ae.onclick=function(){m&&d()};var ye=document.createElement("div");ye.id=H,ye.style.boxSizing="border-box",ye.style.width="100%",ye.style.padding="15px",ye.style.display="block",ye.style.cursor="default",ye.style.backgroundColor=T,de.appendChild(ye);var re=document.createElement("div");re.id=I,re.style.cssFloat="left",re.style.height="50px",re.style.lineHeight="50px",re.style.width="50%",re.style.cursor="pointer",re.style.backgroundColor=k,de.appendChild(re);var ce=document.createElement("div");ce.id=R,ce.style.cssFloat="right",ce.style.height="50px",ce.style.lineHeight="50px",ce.style.width="50%",ce.style.cursor="pointer",ce.style.backgroundColor=z,ce.onclick=function(){d()},de.appendChild(ce);var ue=document.createElement("span");ue.id=j,ue.style.color=E,ue.style.fontWeight="600",window.innerWidth<=f?ue.style.fontSize=u:ue.style.fontSize=p,window.addEventListener("resize",Z(X.bind(null,ue),Y),!0),ye.appendChild(ue);var pe=document.createElement("span");pe.id=q,pe.style.color=C,pe.style.fontWeight="600",window.innerWidth<=f?pe.style.fontSize=u:pe.style.fontSize=p,window.addEventListener("resize",Z(X.bind(null,pe),Y),!0),re.appendChild(pe);var fe=document.createElement("span");fe.id=B,fe.style.color=S,fe.style.fontWeight="600",window.innerWidth<=f?fe.style.fontSize=u:fe.style.fontSize=p,window.addEventListener("resize",Z(X.bind(null,fe),Y),!0),ce.appendChild(fe),document.body.appendChild(de),document.body.appendChild(ae);var he=!1,me=document.createElement("div");me.id=D,me.style.position="fixed",me.style.top="0",me.style.left="0",me.style.zIndex="999999998",me.style.height="auto",me.style.width="100%",me.style.display="none",me.style.textAlign="center",me.style.MozTransition="",me.style.WebkitTransition="",me.style.transition="";var be=document.createElement("div");be.id=J,be.style.position="fixed",be.style.top="0",be.style.left="0",be.style.zIndex="999999997",be.style.height="100%",be.style.width="100%",be.style.display="none",be.style.backgroundColor="white",be.style.MozTransition="all "+h+"s ease",be.style.WebkitTransition="all "+h+"s ease",be.style.transition="all "+h+"s ease",be.style.opacity="0",be.onclick=function(){m&&r()};var ve=document.createElement("div");ve.id=G,ve.style.boxSizing="border-box",ve.style.width="100%",ve.style.padding="20px",ve.style.display="block",ve.style.cursor="default",ve.style.backgroundColor=T,me.appendChild(ve);var we=document.createElement("div");we.id=K,we.style.boxSizing="border-box",we.style.height="55px",we.style.width="100%",we.style.display="block",we.style.cursor="default",we.style.backgroundColor="#FFF",me.appendChild(we);var xe=document.createElement("input");xe.id=N,xe.setAttribute("autocomplete","off"),xe.setAttribute("autocorrect","off"),xe.setAttribute("autocapitalize","off"),xe.setAttribute("spellcheck","false"),xe.style.boxSizing="border-box",xe.style.height="55px",xe.style.width="100%",xe.style.textAlign="center",xe.style.textIndent="10px",xe.style.paddingRight="10px",xe.style.outline="0",xe.style.border="0",xe.style.fontFamily="inherit",xe.style.fontSize=p,window.innerWidth<=f?xe.style.fontSize=u:xe.style.fontSize=p,window.addEventListener("resize",Z(X.bind(null,xe),Y),!0),we.appendChild(xe);var ge=document.createElement("div");ge.id=O,ge.style.cssFloat="left",ge.style.height="50px",ge.style.lineHeight="50px",ge.style.width="50%",ge.style.cursor="pointer",ge.style.fontWeight="600",ge.style.backgroundColor=k,me.appendChild(ge);var Te=document.createElement("div");Te.id=P,Te.style.cssFloat="right",Te.style.height="50px",Te.style.lineHeight="50px",Te.style.width="50%",Te.style.cursor="pointer",Te.style.fontWeight="600",Te.style.backgroundColor=z,Te.onclick=function(){r()},me.appendChild(Te);var ke=document.createElement("span");ke.id=Q,ke.style.color=E,ke.style.fontWeight="600",window.innerWidth<=f?ke.style.fontSize=u:ke.style.fontSize=p,window.addEventListener("resize",Z(X.bind(null,ke),Y),!0),ve.appendChild(ke);var ze=document.createElement("span");ze.id=U,ze.style.color=C,window.innerWidth<=f?ze.style.fontSize=u:ze.style.fontSize=p,window.addEventListener("resize",Z(X.bind(null,ze),Y),!0),ge.appendChild(ze);var Ee=document.createElement("span");Ee.id=V,Ee.style.color=S,window.innerWidth<=f?Ee.style.fontSize=u:Ee.style.fontSize=p,window.addEventListener("resize",Z(X.bind(null,Ee),Y),!0),Te.appendChild(Ee),document.body.appendChild(me),document.body.appendChild(be);var Ce=!1;return{alert:n,confirm:l,input:a}}();"undefined"!=typeof module&&module&&(module.exports=notie);