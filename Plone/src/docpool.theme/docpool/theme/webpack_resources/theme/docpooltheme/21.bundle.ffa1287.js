(window.webpackJsonp=window.webpackJsonp||[]).push([[21],{221:function(t,e,p){var a,o;a=[p(1),p(47),p(59),p(43)],void 0===(o=function(t,e,p,a){"use strict";return e.extend({className:"popover upload",title:t.template('<%- _t("Upload files") %>'),content:t.template('<input type="text" name="upload" style="display:none" /><div class="uploadify-me"></div>'),popover:void 0,initialize:function(t){this.app=t.app,e.prototype.initialize.apply(this,[t])},render:function(){var t=this;t.popover=e.prototype.render.call(this);var o={success:function(e,p){var o=p.UID;if(o)new a.QueryHelper({vocabularyUrl:t.app.options.vocabularyUrl,attributes:t.app.options.attributes}).search("UID","plone.app.querystring.operation.selection.is",o,(function(e){var p=t.app.$el.select2("data");p.push.apply(p,e.results),t.app.$el.select2("data",p,!0),t.app.emit("selected"),t.popover.hide()}),!1)},uploadMultiple:!0,allowPathSelection:!1,relativePath:"fileUpload"};return o.baseUrl=t.app.options.rootUrl,t.upload=new p(t.$(".uploadify-me").addClass("pat-upload"),o),this},toggle:function(t,p){e.prototype.toggle.apply(this,[t,p]);this.opened&&this.app.currentPath!==this.upload.currentPath&&this.upload.setPath(this.app.currentPath)}})}.apply(e,a))||(t.exports=o)}}]);