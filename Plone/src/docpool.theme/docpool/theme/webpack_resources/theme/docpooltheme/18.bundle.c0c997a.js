(window.webpackJsonp=window.webpackJsonp||[]).push([[18],{33:function(t,e,i){var o,n;o=[i(44)],void 0===(n=function(t){"use strict";var e=function(){return t.apply(this,arguments)};for(var i in t)t.hasOwnProperty(i)&&(e[i]=t[i]);return(e.prototype=t.prototype).constructor=e,e.extend=function(){console.log("Usage of the mockup-patterns-base pattern is deprecated and it will eventually be removed.Instead, use pat-base and explicitly set parser to 'mockup' when calling extend.");var e=t.extend.apply(this,arguments);return e.prototype.parser="mockup",e},e}.apply(e,o))||(t.exports=n)},34:function(t,e,i){var o,n;o=[i(44)],void 0===(n=function(t){"use strict";return t.extend({name:"cookietrigger",trigger:".pat-cookietrigger",parser:"mockup",isCookiesEnabled:function(){var t="areYourCookiesEnabled=0";document.cookie=t;var e=document.cookie;return-1===e.indexOf(t)?0:(t="areYourCookiesEnabled=1",document.cookie=t,-1===(e=document.cookie).indexOf(t)?0:(document.cookie="areYourCookiesEnabled=; expires=Thu, 01-Jan-70 00:00:01 GMT",1))},showIfCookiesDisabled:function(){this.isCookiesEnabled()?this.$el.hide():this.$el.show()},init:function(){this.showIfCookiesDisabled()}})}.apply(e,o))||(t.exports=n)},35:function(t,e,i){var o,n;o=[i(0),i(44),i(45)],void 0===(n=function(t,e,i){"use strict";return e.extend({name:"formunloadalert",trigger:".pat-formunloadalert",parser:"mockup",_changed:!1,_suppressed:!1,defaults:{message:i("Discard changes? If you click OK, any changes you have made will be lost."),changingEvents:"change keyup paste",changingFields:"input,select,textarea,fileupload"},init:function(){var e=this;if(e.$el.is("form")){t(e.options.changingFields,e.$el).on(e.options.changingEvents,(function(t){e._changed=!0}));var i=e.$el.parents(".plone-modal");0!==i.size()?i.data("patternPloneModal").on("hide",(function(t){var o=i.data("patternPloneModal");o&&(o._suppressHide=e._handleUnload.call(e,t))})):t(window).on("beforeunload",(function(t){return e._handleUnload(t)})),e.$el.on("submit",(function(t){e._suppressed=!0}))}},_handleUnload:function(e){if(this._suppressed)this._suppressed=!1;else if(this._changed){var i=this.options.message;return this._handleMsg(e,i),t(window).trigger("messageset"),i}},_handleMsg:function(t,e){(t||window.event).returnValue=e}})}.apply(e,o))||(t.exports=n)},36:function(t,e,i){var o,n;o=[i(0),i(44),i(45)],void 0===(n=function(t,e,i){"use strict";return e.extend({name:"preventdoublesubmit",trigger:".pat-preventdoublesubmit",parser:"mockup",defaults:{message:i("You already clicked the submit button. Do you really want to submit this form again?"),guardClassName:"submitting",optOutClassName:"allowMultiSubmit"},init:function(){var e=this;e.$el.is("form")&&t(":submit",e.$el).click((function(i){if(t(":submit").removeAttr("clicked"),t(this).attr("clicked","clicked"),t(this).hasClass(e.options.guardClassName)&&!t(this).hasClass(e.options.optOutClassName))return e._confirm.call(e);t(this).addClass(e.options.guardClassName)}))},_confirm:function(t){return window.confirm(this.options.message)}})}.apply(e,o))||(t.exports=n)},37:function(t,e,i){var o,n;o=[i(0),i(44)],void 0===(n=function(t,e,i){"use strict";return e.extend({name:"formautofocus",trigger:".pat-formautofocus",parser:"mockup",defaults:{condition:"div.error",target:"div.error :input:not(.formTabs):visible:first",always:":input:not(.formTabs):visible:first"},init:function(){0!==t(this.options.condition,this.$el).size()?t(this.options.target,this.$el).focus():t(this.options.always,this.$el).focus()}})}.apply(e,o))||(t.exports=n)},38:function(t,e,i){var o,n;o=[i(44),i(0)],void 0===(n=function(t,e){"use strict";return t.extend({name:"markspeciallinks",trigger:".pat-markspeciallinks",parser:"mockup",defaults:{external_links_open_new_window:!1,mark_special_links:!0},init:function(){var t,i,o,n,s,a,r=this.$el;"string"==typeof this.options.external_links_open_new_window?t="true"===this.options.external_links_open_new_window.toLowerCase():"boolean"==typeof this.options.external_links_open_new_window&&(t=this.options.external_links_open_new_window),"string"==typeof this.options.mark_special_links?i="true"===this.options.mark_special_links.toLowerCase():"boolean"==typeof this.options.mark_special_links&&(i=this.options.mark_special_links),o=window.location.protocol+"//"+window.location.host,n=/^(mailto|ftp|news|irc|h323|sip|callto|https|feed|webcal)/,s=r,t&&s.find('a[href^="http"]:not(.link-plain):not([href^="'+o+'"])').attr("target","_blank").attr("rel","noopener"),i&&(s.find('a[href^="http:"]:not(.link-plain):not([href^="'+o+'"]):not(:has(img))').before('<i class="glyphicon link-external"></i>'),s.find('a[href]:not([href^="http:"]):not(.link-plain):not([href^="'+o+'"]):not(:has(img)):not([href^="#"])').each((function(){if(a=n.exec(e(this).attr("href"))){var t="glyphicon link-"+a[0];e(this).before('<i class="'+t+'"></i>')}})))}})}.apply(e,o))||(t.exports=n)},39:function(t,e,i){var o,n;o=[i(0),i(44),i(1),i(45)],void 0===(n=function(t,e,i,o){"use strict";return e.extend({name:"livesearch",trigger:".pat-livesearch",parser:"mockup",timeout:null,active:!1,results:null,selectedItem:-1,resultsClass:"livesearch-results",defaults:{ajaxUrl:null,defaultSortOn:"",perPage:7,quietMillis:350,minimumInputLength:4,inputSelector:'input[type="text"]',itemTemplate:'<li class="search-result <%- state %>"><h4 class="title"><a href="<%- url %>"><%- title %></a></h4><p class="description"><%- description %></p></li>'},doSearch:function(e){var i=this;i.active=!0,i.render(),i.$el.addClass("searching");var n=i.$el.serialize();void 0===e&&(e=1);var s=function(){var e=location.search,o=e.indexOf("sort_on");if(-1===o){var n=t("#search-results");return n.length>0?n.attr("data-default-sort"):i.options.defaultSortOn}var s=e.substring(o);return s=(s=s.split("&")[0]).split("=")[1]}();t.ajax({url:i.options.ajaxUrl+"?"+n+"&page="+e+"&perPage="+i.options.perPage+"&sort_on="+s,dataType:"json"}).done((function(t){i.results=t,i.page=e,n!==i.$el.serialize()&&i.doSearch()})).fail((function(){i.results={items:[{url:"",title:o("Error"),description:o("There was an error searching…"),state:"error",error:!1}],total:1},i.page=1})).always((function(){i.active=!1,i.selectedItem=-1,i.$el.removeClass("searching"),i.render()}))},render:function(){var e=this;if(e.$results.empty(),e.active?e.$results.append(t('<li class="searching">'+o("searching…")+"</li>")):null===e.results?e.$results.append(t('<li class="no-results no-search">'+o("enter search phrase")+"</li>")):0===e.results.total?e.$results.append(t('<li class="no-results">'+o("no results found")+"</li>")):e.$results.append(t('<li class="results-summary">'+o("found")+" "+e.results.total+" "+o("results")+"</li>")),null!==e.results){var n=i.template(e.options.itemTemplate);i.each(e.results.items,(function(i,s){var a=t(n(t.extend({_t:o},i)));a.attr("data-url",i.url).on("click",(function(){i.error||(window.location=i.url)})),s===e.selectedItem&&a.addClass("selected"),e.$results.append(a)}));var s=[];if(e.page>1){var a=t('<a href="#" class="prev">'+o("Previous")+"</a>");a.click((function(t){e.disableHiding=!0,t.preventDefault(),e.doSearch(e.page-1)})),s.push(a)}if(e.page*e.options.perPage<e.results.total){var r=t('<a href="#" class="next">'+o("Next")+"</a>");r.click((function(t){e.disableHiding=!0,t.preventDefault(),e.doSearch(e.page+1)})),s.push(r)}if(s.length>0){var l=t('<li class="load-more"><div class="page">'+e.page+"</div></li>");l.prepend(s),e.$results.append(l)}}e.position()},position:function(){this.$el.addClass("livesearch-active");var t=this.$input.position();this.$results.width(this.$el.outerWidth()),this.$results.css({top:t.top+this.$input.outerHeight(),left:t.left}),this.$results.show()},hide:function(){this.$results.hide(),this.$el.removeClass("livesearch-active")},init:function(){var e=this;e.$input=e.$el.find(e.options.inputSelector),e.$input.off("focusout").on("focusout",(function(){setTimeout((function(){e.disableHiding?(e.disableHiding=!1,e.$input.focus()):e.hide()}),200)})).off("focusin").on("focusin",(function(){e.onceFocused?e.$results.is(":visible")||e.render():(e.onceFocused=!0,e.$input.val().length>=e.options.minimumInputLength&&e.doSearch())})).attr("autocomplete","off").off("keyup").on("keyup",(function(t){var i=t.keyCode||t.which;if(27===i)return e.$input.val(""),void e.hide();if(e.results&&e.results.items&&e.results.items.length>0){if(13===i)return void(-1!==e.selectedItem&&(window.location=e.results.items[e.selectedItem].url));if(38===i)return void(-1!==e.selectedItem&&(e.selectedItem-=1,e.render()));if(40===i)return void(e.selectedItem<e.results.items.length&&(e.selectedItem+=1,e.render()))}null!==e.timeout&&(clearTimeout(e.timeout),e.timeout=null),e.active||(e.$input.val().length>=e.options.minimumInputLength?e.timeout=setTimeout((function(){e.doSearch()}),e.options.quietMillis):(e.results=null,e.render()))})),t("#sorting-options a").click((function(t){t.preventDefault(),e.onceFocused=!1})),e.$results=t('<ul class="'+e.resultsClass+'"></ul>').hide().insertAfter(e.$input)}})}.apply(e,o))||(t.exports=n)},40:function(t,e,i){var o,n;o=[i(0),i(44),i(4),i(2),i(46),i(1)],void 0===(n=function(t,e,i,o,n,s){"use strict";var a=i.getLogger("pat-contentloader");return e.extend({name:"contentloader",trigger:".pat-contentloader",parser:"mockup",defaults:{url:null,content:null,trigger:"click",target:null,template:null,dataType:"html"},init:function(){var t=this;"el"===t.options.url&&"A"===t.$el[0].tagName&&(t.options.url=t.$el.attr("href")),t.$el.removeClass("loading-content"),t.$el.removeClass("content-load-error"),"immediate"===t.options.trigger?t._load():t.$el.on(t.options.trigger,(function(e){e.preventDefault(),t._load()}))},_load:function(){this.$el.addClass("loading-content"),this.options.url?this.loadRemote():this.loadLocal()},loadRemote:function(){var e=this;t.ajax({url:e.options.url,dataType:e.options.dataType,success:function(i){var o;if("html"===e.options.dataType)-1!==i.indexOf("<html")&&(i=n.parseBodyTag(i)),o=t("<div>"+i+"</div>");else if(-1!==e.options.dataType.indexOf("json")){i.constructor===Array&&1===i.length&&(i=i[0]);try{o=t(s.template(e.options.template)(i))}catch(t){return e.$el.removeClass("loading-content"),e.$el.addClass("content-load-error"),void a.warn("error rendering template. pat-contentloader will not work")}}null!==e.options.content&&(o=o.find(e.options.content)),e.loadLocal(o)},error:function(){e.$el.removeClass("loading-content"),e.$el.addClass("content-load-error")}})},loadLocal:function(e){if(!e&&null===this.options.content)return this.$el.removeClass("loading-content"),this.$el.addClass("content-load-error"),void a.warn("No selector configured");var i=this.$el;if(null!==this.options.target&&0===(i=t(this.options.target)).size())return this.$el.removeClass("loading-content"),this.$el.addClass("content-load-error"),void a.warn("No target nodes found");e||(e=t(this.options.content).clone()),e.length?(e.show(),i.replaceWith(e),o.scan(e)):i.empty(),this.$el.removeClass("loading-content"),this.emit("loading-done")}})}.apply(e,o))||(t.exports=n)},41:function(t,e,i){!function(t){"use strict";var e=function(i,o){this.$element=t(i),this.options=t.extend({},e.DEFAULTS,o),this.$trigger=t('[data-toggle="collapse"][href="#'+i.id+'"],[data-toggle="collapse"][data-target="#'+i.id+'"]'),this.transitioning=null,this.options.parent?this.$parent=this.getParent():this.addAriaAndCollapsedClass(this.$element,this.$trigger),this.options.toggle&&this.toggle()};function i(e){var i,o=e.attr("data-target")||(i=e.attr("href"))&&i.replace(/.*(?=#[^\s]+$)/,"");return t(o)}function o(i){return this.each((function(){var o=t(this),n=o.data("bs.collapse"),s=t.extend({},e.DEFAULTS,o.data(),"object"==typeof i&&i);!n&&s.toggle&&/show|hide/.test(i)&&(s.toggle=!1),n||o.data("bs.collapse",n=new e(this,s)),"string"==typeof i&&n[i]()}))}e.VERSION="3.3.6",e.TRANSITION_DURATION=350,e.DEFAULTS={toggle:!0},e.prototype.dimension=function(){return this.$element.hasClass("width")?"width":"height"},e.prototype.show=function(){if(!this.transitioning&&!this.$element.hasClass("in")){var i,n=this.$parent&&this.$parent.children(".panel").children(".in, .collapsing");if(!(n&&n.length&&(i=n.data("bs.collapse"))&&i.transitioning)){var s=t.Event("show.bs.collapse");if(this.$element.trigger(s),!s.isDefaultPrevented()){n&&n.length&&(o.call(n,"hide"),i||n.data("bs.collapse",null));var a=this.dimension();this.$element.removeClass("collapse").addClass("collapsing")[a](0).attr("aria-expanded",!0),this.$trigger.removeClass("collapsed").attr("aria-expanded",!0),this.transitioning=1;var r=function(){this.$element.removeClass("collapsing").addClass("collapse in")[a](""),this.transitioning=0,this.$element.trigger("shown.bs.collapse")};if(!t.support.transition)return r.call(this);var l=t.camelCase(["scroll",a].join("-"));this.$element.one("bsTransitionEnd",t.proxy(r,this)).emulateTransitionEnd(e.TRANSITION_DURATION)[a](this.$element[0][l])}}}},e.prototype.hide=function(){if(!this.transitioning&&this.$element.hasClass("in")){var i=t.Event("hide.bs.collapse");if(this.$element.trigger(i),!i.isDefaultPrevented()){var o=this.dimension();this.$element[o](this.$element[o]())[0].offsetHeight,this.$element.addClass("collapsing").removeClass("collapse in").attr("aria-expanded",!1),this.$trigger.addClass("collapsed").attr("aria-expanded",!1),this.transitioning=1;var n=function(){this.transitioning=0,this.$element.removeClass("collapsing").addClass("collapse").trigger("hidden.bs.collapse")};if(!t.support.transition)return n.call(this);this.$element[o](0).one("bsTransitionEnd",t.proxy(n,this)).emulateTransitionEnd(e.TRANSITION_DURATION)}}},e.prototype.toggle=function(){this[this.$element.hasClass("in")?"hide":"show"]()},e.prototype.getParent=function(){return t(this.options.parent).find('[data-toggle="collapse"][data-parent="'+this.options.parent+'"]').each(t.proxy((function(e,o){var n=t(o);this.addAriaAndCollapsedClass(i(n),n)}),this)).end()},e.prototype.addAriaAndCollapsedClass=function(t,e){var i=t.hasClass("in");t.attr("aria-expanded",i),e.toggleClass("collapsed",!i).attr("aria-expanded",i)};var n=t.fn.collapse;t.fn.collapse=o,t.fn.collapse.Constructor=e,t.fn.collapse.noConflict=function(){return t.fn.collapse=n,this},t(document).on("click.bs.collapse.data-api",'[data-toggle="collapse"]',(function(e){var n=t(this);n.attr("data-target")||e.preventDefault();var s=i(n),a=s.data("bs.collapse")?"toggle":n.data();o.call(s,a)}))}(i(0))},42:function(t,e,i){!function(t){"use strict";var e=function(t,e){this.type=null,this.options=null,this.enabled=null,this.timeout=null,this.hoverState=null,this.$element=null,this.inState=null,this.init("tooltip",t,e)};e.VERSION="3.3.6",e.TRANSITION_DURATION=150,e.DEFAULTS={animation:!0,placement:"top",selector:!1,template:'<div class="tooltip" role="tooltip"><div class="tooltip-arrow"></div><div class="tooltip-inner"></div></div>',trigger:"hover focus",title:"",delay:0,html:!1,container:!1,viewport:{selector:"body",padding:0}},e.prototype.init=function(e,i,o){if(this.enabled=!0,this.type=e,this.$element=t(i),this.options=this.getOptions(o),this.$viewport=this.options.viewport&&t(t.isFunction(this.options.viewport)?this.options.viewport.call(this,this.$element):this.options.viewport.selector||this.options.viewport),this.inState={click:!1,hover:!1,focus:!1},this.$element[0]instanceof document.constructor&&!this.options.selector)throw new Error("`selector` option must be specified when initializing "+this.type+" on the window.document object!");for(var n=this.options.trigger.split(" "),s=n.length;s--;){var a=n[s];if("click"==a)this.$element.on("click."+this.type,this.options.selector,t.proxy(this.toggle,this));else if("manual"!=a){var r="hover"==a?"mouseenter":"focusin",l="hover"==a?"mouseleave":"focusout";this.$element.on(r+"."+this.type,this.options.selector,t.proxy(this.enter,this)),this.$element.on(l+"."+this.type,this.options.selector,t.proxy(this.leave,this))}}this.options.selector?this._options=t.extend({},this.options,{trigger:"manual",selector:""}):this.fixTitle()},e.prototype.getDefaults=function(){return e.DEFAULTS},e.prototype.getOptions=function(e){return(e=t.extend({},this.getDefaults(),this.$element.data(),e)).delay&&"number"==typeof e.delay&&(e.delay={show:e.delay,hide:e.delay}),e},e.prototype.getDelegateOptions=function(){var e={},i=this.getDefaults();return this._options&&t.each(this._options,(function(t,o){i[t]!=o&&(e[t]=o)})),e},e.prototype.enter=function(e){var i=e instanceof this.constructor?e:t(e.currentTarget).data("bs."+this.type);if(i||(i=new this.constructor(e.currentTarget,this.getDelegateOptions()),t(e.currentTarget).data("bs."+this.type,i)),e instanceof t.Event&&(i.inState["focusin"==e.type?"focus":"hover"]=!0),i.tip().hasClass("in")||"in"==i.hoverState)i.hoverState="in";else{if(clearTimeout(i.timeout),i.hoverState="in",!i.options.delay||!i.options.delay.show)return i.show();i.timeout=setTimeout((function(){"in"==i.hoverState&&i.show()}),i.options.delay.show)}},e.prototype.isInStateTrue=function(){for(var t in this.inState)if(this.inState[t])return!0;return!1},e.prototype.leave=function(e){var i=e instanceof this.constructor?e:t(e.currentTarget).data("bs."+this.type);if(i||(i=new this.constructor(e.currentTarget,this.getDelegateOptions()),t(e.currentTarget).data("bs."+this.type,i)),e instanceof t.Event&&(i.inState["focusout"==e.type?"focus":"hover"]=!1),!i.isInStateTrue()){if(clearTimeout(i.timeout),i.hoverState="out",!i.options.delay||!i.options.delay.hide)return i.hide();i.timeout=setTimeout((function(){"out"==i.hoverState&&i.hide()}),i.options.delay.hide)}},e.prototype.show=function(){var i=t.Event("show.bs."+this.type);if(this.hasContent()&&this.enabled){this.$element.trigger(i);var o=t.contains(this.$element[0].ownerDocument.documentElement,this.$element[0]);if(i.isDefaultPrevented()||!o)return;var n=this,s=this.tip(),a=this.getUID(this.type);this.setContent(),s.attr("id",a),this.$element.attr("aria-describedby",a),this.options.animation&&s.addClass("fade");var r="function"==typeof this.options.placement?this.options.placement.call(this,s[0],this.$element[0]):this.options.placement,l=/\s?auto?\s?/i,p=l.test(r);p&&(r=r.replace(l,"")||"top"),s.detach().css({top:0,left:0,display:"block"}).addClass(r).data("bs."+this.type,this),this.options.container?s.appendTo(this.options.container):s.insertAfter(this.$element),this.$element.trigger("inserted.bs."+this.type);var h=this.getPosition(),c=s[0].offsetWidth,u=s[0].offsetHeight;if(p){var d=r,f=this.getPosition(this.$viewport);r="bottom"==r&&h.bottom+u>f.bottom?"top":"top"==r&&h.top-u<f.top?"bottom":"right"==r&&h.right+c>f.width?"left":"left"==r&&h.left-c<f.left?"right":r,s.removeClass(d).addClass(r)}var g=this.getCalculatedOffset(r,h,c,u);this.applyPlacement(g,r);var m=function(){var t=n.hoverState;n.$element.trigger("shown.bs."+n.type),n.hoverState=null,"out"==t&&n.leave(n)};t.support.transition&&this.$tip.hasClass("fade")?s.one("bsTransitionEnd",m).emulateTransitionEnd(e.TRANSITION_DURATION):m()}},e.prototype.applyPlacement=function(e,i){var o=this.tip(),n=o[0].offsetWidth,s=o[0].offsetHeight,a=parseInt(o.css("margin-top"),10),r=parseInt(o.css("margin-left"),10);isNaN(a)&&(a=0),isNaN(r)&&(r=0),e.top+=a,e.left+=r,t.offset.setOffset(o[0],t.extend({using:function(t){o.css({top:Math.round(t.top),left:Math.round(t.left)})}},e),0),o.addClass("in");var l=o[0].offsetWidth,p=o[0].offsetHeight;"top"==i&&p!=s&&(e.top=e.top+s-p);var h=this.getViewportAdjustedDelta(i,e,l,p);h.left?e.left+=h.left:e.top+=h.top;var c=/top|bottom/.test(i),u=c?2*h.left-n+l:2*h.top-s+p,d=c?"offsetWidth":"offsetHeight";o.offset(e),this.replaceArrow(u,o[0][d],c)},e.prototype.replaceArrow=function(t,e,i){this.arrow().css(i?"left":"top",50*(1-t/e)+"%").css(i?"top":"left","")},e.prototype.setContent=function(){var t=this.tip(),e=this.getTitle();t.find(".tooltip-inner")[this.options.html?"html":"text"](e),t.removeClass("fade in top bottom left right")},e.prototype.hide=function(i){var o=this,n=t(this.$tip),s=t.Event("hide.bs."+this.type);function a(){"in"!=o.hoverState&&n.detach(),o.$element.removeAttr("aria-describedby").trigger("hidden.bs."+o.type),i&&i()}if(this.$element.trigger(s),!s.isDefaultPrevented())return n.removeClass("in"),t.support.transition&&n.hasClass("fade")?n.one("bsTransitionEnd",a).emulateTransitionEnd(e.TRANSITION_DURATION):a(),this.hoverState=null,this},e.prototype.fixTitle=function(){var t=this.$element;(t.attr("title")||"string"!=typeof t.attr("data-original-title"))&&t.attr("data-original-title",t.attr("title")||"").attr("title","")},e.prototype.hasContent=function(){return this.getTitle()},e.prototype.getPosition=function(e){var i=(e=e||this.$element)[0],o="BODY"==i.tagName,n=i.getBoundingClientRect();null==n.width&&(n=t.extend({},n,{width:n.right-n.left,height:n.bottom-n.top}));var s=o?{top:0,left:0}:e.offset(),a={scroll:o?document.documentElement.scrollTop||document.body.scrollTop:e.scrollTop()},r=o?{width:t(window).width(),height:t(window).height()}:null;return t.extend({},n,a,r,s)},e.prototype.getCalculatedOffset=function(t,e,i,o){return"bottom"==t?{top:e.top+e.height,left:e.left+e.width/2-i/2}:"top"==t?{top:e.top-o,left:e.left+e.width/2-i/2}:"left"==t?{top:e.top+e.height/2-o/2,left:e.left-i}:{top:e.top+e.height/2-o/2,left:e.left+e.width}},e.prototype.getViewportAdjustedDelta=function(t,e,i,o){var n={top:0,left:0};if(!this.$viewport)return n;var s=this.options.viewport&&this.options.viewport.padding||0,a=this.getPosition(this.$viewport);if(/right|left/.test(t)){var r=e.top-s-a.scroll,l=e.top+s-a.scroll+o;r<a.top?n.top=a.top-r:l>a.top+a.height&&(n.top=a.top+a.height-l)}else{var p=e.left-s,h=e.left+s+i;p<a.left?n.left=a.left-p:h>a.right&&(n.left=a.left+a.width-h)}return n},e.prototype.getTitle=function(){var t=this.$element,e=this.options;return t.attr("data-original-title")||("function"==typeof e.title?e.title.call(t[0]):e.title)},e.prototype.getUID=function(t){do{t+=~~(1e6*Math.random())}while(document.getElementById(t));return t},e.prototype.tip=function(){if(!this.$tip&&(this.$tip=t(this.options.template),1!=this.$tip.length))throw new Error(this.type+" `template` option must consist of exactly 1 top-level element!");return this.$tip},e.prototype.arrow=function(){return this.$arrow=this.$arrow||this.tip().find(".tooltip-arrow")},e.prototype.enable=function(){this.enabled=!0},e.prototype.disable=function(){this.enabled=!1},e.prototype.toggleEnabled=function(){this.enabled=!this.enabled},e.prototype.toggle=function(e){var i=this;e&&((i=t(e.currentTarget).data("bs."+this.type))||(i=new this.constructor(e.currentTarget,this.getDelegateOptions()),t(e.currentTarget).data("bs."+this.type,i))),e?(i.inState.click=!i.inState.click,i.isInStateTrue()?i.enter(i):i.leave(i)):i.tip().hasClass("in")?i.leave(i):i.enter(i)},e.prototype.destroy=function(){var t=this;clearTimeout(this.timeout),this.hide((function(){t.$element.off("."+t.type).removeData("bs."+t.type),t.$tip&&t.$tip.detach(),t.$tip=null,t.$arrow=null,t.$viewport=null}))};var i=t.fn.tooltip;t.fn.tooltip=function(i){return this.each((function(){var o=t(this),n=o.data("bs.tooltip"),s="object"==typeof i&&i;!n&&/destroy|hide/.test(i)||(n||o.data("bs.tooltip",n=new e(this,s)),"string"==typeof i&&n[i]())}))},t.fn.tooltip.Constructor=e,t.fn.tooltip.noConflict=function(){return t.fn.tooltip=i,this}}(i(0))}}]);