!function(e){"function"==typeof define&&define.amd?define(["jquery"],e):"object"==typeof exports?module.exports=e(require("jquery")):e(jQuery)}(function(e){e.fn.jScrollPane=function(t){function n(t,n){function i(n){var s,a,l,p,u,h,j=!1,g=!1;if(F=n,void 0===L)u=t.scrollTop(),h=t.scrollLeft(),t.css({overflow:"hidden",padding:0}),q=t.innerWidth()+ve,O=t.innerHeight(),t.width(q),L=e('<div class="jspPane" />').css("padding",ge).append(t.children()),E=e('<div class="jspContainer" />').css({width:q+"px",height:O+"px"}).append(L).appendTo(t);else{if(t.css("width",""),j=F.stickToBottom&&D(),g=F.stickToRight&&x(),p=t.innerWidth()+ve!=q||t.outerHeight()!=O,p&&(q=t.innerWidth()+ve,O=t.innerHeight(),E.css({width:q+"px",height:O+"px"})),!p&&me==V&&L.outerHeight()==G)return void t.width(q);me=V,L.css("width",""),t.width(q),E.find(">.jspVerticalBar,>.jspHorizontalBar").remove().end()}L.css("overflow","auto"),V=n.contentWidth?n.contentWidth:L[0].scrollWidth,G=L[0].scrollHeight,L.css("overflow",""),N=V/q,K=G/O,Q=K>1,U=N>1,U||Q?(t.addClass("jspScrollable"),s=F.maintainPosition&&(Z||te),s&&(a=T(),l=B()),o(),r(),c(),s&&(k(g?V-q:a,!1),y(j?G-O:l,!1)),A(),H(),R(),F.enableKeyboardNavigation&&Y(),F.clickOnTrack&&d(),M(),F.hijackInternalLinks&&X()):(t.removeClass("jspScrollable"),L.css({top:0,left:0,width:E.width()-ve}),P(),W(),z(),f()),F.autoReinitialise&&!je?je=setInterval(function(){i(F)},F.autoReinitialiseDelay):!F.autoReinitialise&&je&&clearInterval(je),u&&t.scrollTop(0)&&y(u,!1),h&&t.scrollLeft(0)&&k(h,!1),t.trigger("jsp-initialised",[U||Q])}function o(){Q&&(E.append(e('<div class="jspVerticalBar" />').append(e('<div class="jspCap jspCapTop" />'),e('<div class="jspTrack" />').append(e('<div class="jspDrag" />').append(e('<div class="jspDragTop" />'),e('<div class="jspDragBottom" />'))),e('<div class="jspCap jspCapBottom" />'))),ne=E.find(">.jspVerticalBar"),ie=ne.find(">.jspTrack"),$=ie.find(">.jspDrag"),F.showArrows&&(ae=e('<a class="jspArrow jspArrowUp" />').bind("mousedown.jsp",p(0,-1)).bind("click.jsp",S),ce=e('<a class="jspArrow jspArrowDown" />').bind("mousedown.jsp",p(0,1)).bind("click.jsp",S),F.arrowScrollOnHover&&(ae.bind("mouseover.jsp",p(0,-1,ae)),ce.bind("mouseover.jsp",p(0,1,ce))),l(ie,F.verticalArrowPositions,ae,ce)),se=O,E.find(">.jspVerticalBar>.jspCap:visible,>.jspVerticalBar>.jspArrow").each(function(){se-=e(this).outerHeight()}),$.hover(function(){$.addClass("jspHover")},function(){$.removeClass("jspHover")}).bind("mousedown.jsp",function(t){e("html").bind("dragstart.jsp selectstart.jsp",S),$.addClass("jspActive");var n=t.pageY-$.position().top;return e("html").bind("mousemove.jsp",function(e){j(e.pageY-n,!1)}).bind("mouseup.jsp mouseleave.jsp",h),!1}),s())}function s(){ie.height(se+"px"),Z=0,oe=F.verticalGutter+ie.outerWidth(),L.width(q-oe-ve);try{0===ne.position().left&&L.css("margin-left",oe+"px")}catch(e){}}function r(){U&&(E.append(e('<div class="jspHorizontalBar" />').append(e('<div class="jspCap jspCapLeft" />'),e('<div class="jspTrack" />').append(e('<div class="jspDrag" />').append(e('<div class="jspDragLeft" />'),e('<div class="jspDragRight" />'))),e('<div class="jspCap jspCapRight" />'))),le=E.find(">.jspHorizontalBar"),pe=le.find(">.jspTrack"),_=pe.find(">.jspDrag"),F.showArrows&&(fe=e('<a class="jspArrow jspArrowLeft" />').bind("mousedown.jsp",p(-1,0)).bind("click.jsp",S),he=e('<a class="jspArrow jspArrowRight" />').bind("mousedown.jsp",p(1,0)).bind("click.jsp",S),F.arrowScrollOnHover&&(fe.bind("mouseover.jsp",p(-1,0,fe)),he.bind("mouseover.jsp",p(1,0,he))),l(pe,F.horizontalArrowPositions,fe,he)),_.hover(function(){_.addClass("jspHover")},function(){_.removeClass("jspHover")}).bind("mousedown.jsp",function(t){e("html").bind("dragstart.jsp selectstart.jsp",S),_.addClass("jspActive");var n=t.pageX-_.position().left;return e("html").bind("mousemove.jsp",function(e){v(e.pageX-n,!1)}).bind("mouseup.jsp mouseleave.jsp",h),!1}),ue=E.innerWidth(),a())}function a(){E.find(">.jspHorizontalBar>.jspCap:visible,>.jspHorizontalBar>.jspArrow").each(function(){ue-=e(this).outerWidth()}),pe.width(ue+"px"),te=0}function c(){if(U&&Q){var t=pe.outerHeight(),n=ie.outerWidth();se-=t,e(le).find(">.jspCap:visible,>.jspArrow").each(function(){ue+=e(this).outerWidth()}),ue-=n,O-=n,q-=t,pe.parent().append(e('<div class="jspCorner" />').css("width",t+"px")),s(),a()}U&&L.width(E.outerWidth()-ve+"px"),G=L.outerHeight(),K=G/O,U&&(de=Math.ceil(1/N*ue),de>F.horizontalDragMaxWidth?de=F.horizontalDragMaxWidth:de<F.horizontalDragMinWidth&&(de=F.horizontalDragMinWidth),_.width(de+"px"),ee=ue-de,m(te)),Q&&(re=Math.ceil(1/K*se),re>F.verticalDragMaxHeight?re=F.verticalDragMaxHeight:re<F.verticalDragMinHeight&&(re=F.verticalDragMinHeight),$.height(re+"px"),J=se-re,g(Z))}function l(e,t,n,i){var o,s="before",r="after";"os"==t&&(t=/Mac/.test(navigator.platform)?"after":"split"),t==s?r=t:t==r&&(s=t,o=n,n=i,i=o),e[s](n)[r](i)}function p(e,t,n){return function(){return u(e,t,this,n),this.blur(),!1}}function u(t,n,i,o){i=e(i).addClass("jspActive");var s,r,a=!0,c=function(){0!==t&&be.scrollByX(t*F.arrowButtonSpeed),0!==n&&be.scrollByY(n*F.arrowButtonSpeed),r=setTimeout(c,a?F.initialDelay:F.arrowRepeatFreq),a=!1};c(),s=o?"mouseout.jsp":"mouseup.jsp",o=o||e("html"),o.bind(s,function(){i.removeClass("jspActive"),r&&clearTimeout(r),r=null,o.unbind(s)})}function d(){f(),Q&&ie.bind("mousedown.jsp",function(t){if(void 0===t.originalTarget||t.originalTarget==t.currentTarget){var n,i=e(this),o=i.offset(),s=t.pageY-o.top-Z,r=!0,a=function(){var e=i.offset(),o=t.pageY-e.top-re/2,l=O*F.scrollPagePercent,p=J*l/(G-O);if(s<0)Z-p>o?be.scrollByY(-l):j(o);else{if(!(s>0))return void c();Z+p<o?be.scrollByY(l):j(o)}n=setTimeout(a,r?F.initialDelay:F.trackClickRepeatFreq),r=!1},c=function(){n&&clearTimeout(n),n=null,e(document).unbind("mouseup.jsp",c)};return a(),e(document).bind("mouseup.jsp",c),!1}}),U&&pe.bind("mousedown.jsp",function(t){if(void 0===t.originalTarget||t.originalTarget==t.currentTarget){var n,i=e(this),o=i.offset(),s=t.pageX-o.left-te,r=!0,a=function(){var e=i.offset(),o=t.pageX-e.left-de/2,l=q*F.scrollPagePercent,p=ee*l/(V-q);if(s<0)te-p>o?be.scrollByX(-l):v(o);else{if(!(s>0))return void c();te+p<o?be.scrollByX(l):v(o)}n=setTimeout(a,r?F.initialDelay:F.trackClickRepeatFreq),r=!1},c=function(){n&&clearTimeout(n),n=null,e(document).unbind("mouseup.jsp",c)};return a(),e(document).bind("mouseup.jsp",c),!1}})}function f(){pe&&pe.unbind("mousedown.jsp"),ie&&ie.unbind("mousedown.jsp")}function h(){e("html").unbind("dragstart.jsp selectstart.jsp mousemove.jsp mouseup.jsp mouseleave.jsp"),$&&$.removeClass("jspActive"),_&&_.removeClass("jspActive")}function j(n,i){if(Q){n<0?n=0:n>J&&(n=J);var o=new e.Event("jsp-will-scroll-y");if(t.trigger(o,[n]),!o.isDefaultPrevented()){var s=n||0,r=0===s,a=s==J,c=n/J,l=-c*(G-O);void 0===i&&(i=F.animateScroll),i?be.animate($,"top",n,g,function(){t.trigger("jsp-user-scroll-y",[-l,r,a])}):($.css("top",n),g(n),t.trigger("jsp-user-scroll-y",[-l,r,a]))}}}function g(e){void 0===e&&(e=$.position().top),E.scrollTop(0),Z=e||0;var n=0===Z,i=Z==J,o=e/J,s=-o*(G-O);we==n&&ke==i||(we=n,ke=i,t.trigger("jsp-arrow-change",[we,ke,ye,Ce])),b(n,i),L.css("top",s),t.trigger("jsp-scroll-y",[-s,n,i]).trigger("scroll")}function v(n,i){if(U){n<0?n=0:n>ee&&(n=ee);var o=new e.Event("jsp-will-scroll-x");if(t.trigger(o,[n]),!o.isDefaultPrevented()){var s=n||0,r=0===s,a=s==ee,c=n/ee,l=-c*(V-q);void 0===i&&(i=F.animateScroll),i?be.animate(_,"left",n,m,function(){t.trigger("jsp-user-scroll-x",[-l,r,a])}):(_.css("left",n),m(n),t.trigger("jsp-user-scroll-x",[-l,r,a]))}}}function m(e){void 0===e&&(e=_.position().left),E.scrollTop(0),te=e||0;var n=0===te,i=te==ee,o=e/ee,s=-o*(V-q);ye==n&&Ce==i||(ye=n,Ce=i,t.trigger("jsp-arrow-change",[we,ke,ye,Ce])),w(n,i),L.css("left",s),t.trigger("jsp-scroll-x",[-s,n,i]).trigger("scroll")}function b(e,t){F.showArrows&&(ae[e?"addClass":"removeClass"]("jspDisabled"),ce[t?"addClass":"removeClass"]("jspDisabled"))}function w(e,t){F.showArrows&&(fe[e?"addClass":"removeClass"]("jspDisabled"),he[t?"addClass":"removeClass"]("jspDisabled"))}function y(e,t){var n=e/(G-O);j(n*J,t)}function k(e,t){var n=e/(V-q);v(n*ee,t)}function C(t,n,i){var o,s,r,a,c,l,p,u,d,f=0,h=0;try{o=e(t)}catch(j){return}for(s=o.outerHeight(),r=o.outerWidth(),E.scrollTop(0),E.scrollLeft(0);!o.is(".jspPane");)if(f+=o.position().top,h+=o.position().left,o=o.offsetParent(),/^body|html$/i.test(o[0].nodeName))return;a=B(),l=a+O,f<a||n?u=f-F.horizontalGutter:f+s>l&&(u=f-O+s+F.horizontalGutter),isNaN(u)||y(u,i),c=T(),p=c+q,h<c||n?d=h-F.horizontalGutter:h+r>p&&(d=h-q+r+F.horizontalGutter),isNaN(d)||k(d,i)}function T(){return-L.position().left}function B(){return-L.position().top}function D(){var e=G-O;return e>20&&e-B()<10}function x(){var e=V-q;return e>20&&e-T()<10}function H(){E.unbind(Be).bind(Be,function(e,t,n,i){te||(te=0),Z||(Z=0);var o=te,s=Z,r=e.deltaFactor||F.mouseWheelSpeed;return be.scrollBy(n*r,-i*r,!1),o==te&&s==Z})}function P(){E.unbind(Be)}function S(){return!1}function A(){L.find(":input,a").unbind("focus.jsp").bind("focus.jsp",function(e){C(e.target,!1)})}function W(){L.find(":input,a").unbind("focus.jsp")}function Y(){function n(){var e=te,t=Z;switch(i){case 40:be.scrollByY(F.keyboardSpeed,!1);break;case 38:be.scrollByY(-F.keyboardSpeed,!1);break;case 34:case 32:be.scrollByY(O*F.scrollPagePercent,!1);break;case 33:be.scrollByY(-O*F.scrollPagePercent,!1);break;case 39:be.scrollByX(F.keyboardSpeed,!1);break;case 37:be.scrollByX(-F.keyboardSpeed,!1)}return o=e!=te||t!=Z}var i,o,s=[];U&&s.push(le[0]),Q&&s.push(ne[0]),L.bind("focus.jsp",function(){t.focus()}),t.attr("tabindex",0).unbind("keydown.jsp keypress.jsp").bind("keydown.jsp",function(t){if(t.target===this||s.length&&e(t.target).closest(s).length){var r=te,a=Z;switch(t.keyCode){case 40:case 38:case 34:case 32:case 33:case 39:case 37:i=t.keyCode,n();break;case 35:y(G-O),i=null;break;case 36:y(0),i=null}return o=t.keyCode==i&&r!=te||a!=Z,!o}}).bind("keypress.jsp",function(t){if(t.keyCode==i&&n(),t.target===this||s.length&&e(t.target).closest(s).length)return!o}),F.hideFocus?(t.css("outline","none"),"hideFocus"in E[0]&&t.attr("hideFocus",!0)):(t.css("outline",""),"hideFocus"in E[0]&&t.attr("hideFocus",!1))}function z(){t.attr("tabindex","-1").removeAttr("tabindex").unbind("keydown.jsp keypress.jsp"),L.unbind(".jsp")}function M(){if(location.hash&&location.hash.length>1){var t,n,i=escape(location.hash.substr(1));try{t=e("#"+i+', a[name="'+i+'"]')}catch(o){return}t.length&&L.find(i)&&(0===E.scrollTop()?n=setInterval(function(){E.scrollTop()>0&&(C(t,!0),e(document).scrollTop(E.position().top),clearInterval(n))},50):(C(t,!0),e(document).scrollTop(E.position().top)))}}function X(){e(document.body).data("jspHijack")||(e(document.body).data("jspHijack",!0),e(document.body).delegate('a[href*="#"]',"click",function(t){var n,i,o,s,r,a,c=this.href.substr(0,this.href.indexOf("#")),l=location.href;if(location.href.indexOf("#")!==-1&&(l=location.href.substr(0,location.href.indexOf("#"))),c===l){n=escape(this.href.substr(this.href.indexOf("#")+1));try{i=e("#"+n+', a[name="'+n+'"]')}catch(p){return}i.length&&(o=i.closest(".jspScrollable"),s=o.data("jsp"),s.scrollToElement(i,!0),o[0].scrollIntoView&&(r=e(window).scrollTop(),a=i.offset().top,(a<r||a>r+e(window).height())&&o[0].scrollIntoView()),t.preventDefault())}}))}function R(){var e,t,n,i,o,s=!1;E.unbind("touchstart.jsp touchmove.jsp touchend.jsp click.jsp-touchclick").bind("touchstart.jsp",function(r){var a=r.originalEvent.touches[0];e=T(),t=B(),n=a.pageX,i=a.pageY,o=!1,s=!0}).bind("touchmove.jsp",function(r){if(s){var a=r.originalEvent.touches[0],c=te,l=Z;return be.scrollTo(e+n-a.pageX,t+i-a.pageY),o=o||Math.abs(n-a.pageX)>5||Math.abs(i-a.pageY)>5,c==te&&l==Z}}).bind("touchend.jsp",function(e){s=!1}).bind("click.jsp-touchclick",function(e){if(o)return o=!1,!1})}function I(){var e=B(),n=T();t.removeClass("jspScrollable").unbind(".jsp"),L.unbind(".jsp"),t.replaceWith(Te.append(L.children())),Te.scrollTop(e),Te.scrollLeft(n),je&&clearInterval(je)}var F,L,q,O,E,V,G,N,K,Q,U,$,J,Z,_,ee,te,ne,ie,oe,se,re,ae,ce,le,pe,ue,de,fe,he,je,ge,ve,me,be=this,we=!0,ye=!0,ke=!1,Ce=!1,Te=t.clone(!1,!1).empty(),Be=e.fn.mwheelIntent?"mwheelIntent.jsp":"mousewheel.jsp";"border-box"===t.css("box-sizing")?(ge=0,ve=0):(ge=t.css("paddingTop")+" "+t.css("paddingRight")+" "+t.css("paddingBottom")+" "+t.css("paddingLeft"),ve=(parseInt(t.css("paddingLeft"),10)||0)+(parseInt(t.css("paddingRight"),10)||0)),e.extend(be,{reinitialise:function(t){t=e.extend({},F,t),i(t)},scrollToElement:function(e,t,n){C(e,t,n)},scrollTo:function(e,t,n){k(e,n),y(t,n)},scrollToX:function(e,t){k(e,t)},scrollToY:function(e,t){y(e,t)},scrollToPercentX:function(e,t){k(e*(V-q),t)},scrollToPercentY:function(e,t){y(e*(G-O),t)},scrollBy:function(e,t,n){be.scrollByX(e,n),be.scrollByY(t,n)},scrollByX:function(e,t){var n=T()+Math[e<0?"floor":"ceil"](e),i=n/(V-q);v(i*ee,t)},scrollByY:function(e,t){var n=B()+Math[e<0?"floor":"ceil"](e),i=n/(G-O);j(i*J,t)},positionDragX:function(e,t){v(e,t)},positionDragY:function(e,t){j(e,t)},animate:function(e,t,n,i,o){var s={};s[t]=n,e.animate(s,{duration:F.animateDuration,easing:F.animateEase,queue:!1,step:i,complete:o})},getContentPositionX:function(){return T()},getContentPositionY:function(){return B()},getContentWidth:function(){return V},getContentHeight:function(){return G},getPercentScrolledX:function(){return T()/(V-q)},getPercentScrolledY:function(){return B()/(G-O)},getIsScrollableH:function(){return U},getIsScrollableV:function(){return Q},getContentPane:function(){return L},scrollToBottom:function(e){j(J,e)},hijackInternalLinks:e.noop,destroy:function(){I()}}),i(n)}return t=e.extend({},e.fn.jScrollPane.defaults,t),e.each(["arrowButtonSpeed","trackClickSpeed","keyboardSpeed"],function(){t[this]=t[this]||t.speed}),this.each(function(){var i=e(this),o=i.data("jsp");o?o.reinitialise(t):(e("script",i).filter('[type="text/javascript"],:not([type])').remove(),o=new n(i,t),i.data("jsp",o))})},e.fn.jScrollPane.defaults={showArrows:!1,maintainPosition:!0,stickToBottom:!1,stickToRight:!1,clickOnTrack:!0,autoReinitialise:!1,autoReinitialiseDelay:500,verticalDragMinHeight:0,verticalDragMaxHeight:99999,horizontalDragMinWidth:0,horizontalDragMaxWidth:99999,contentWidth:void 0,animateScroll:!1,animateDuration:300,animateEase:"linear",hijackInternalLinks:!1,verticalGutter:4,horizontalGutter:4,mouseWheelSpeed:3,arrowButtonSpeed:0,arrowRepeatFreq:50,arrowScrollOnHover:!1,trackClickSpeed:0,trackClickRepeatFreq:70,verticalArrowPositions:"split",horizontalArrowPositions:"split",enableKeyboardNavigation:!0,hideFocus:!1,keyboardSpeed:0,initialDelay:300,speed:30,scrollPagePercent:.8}});