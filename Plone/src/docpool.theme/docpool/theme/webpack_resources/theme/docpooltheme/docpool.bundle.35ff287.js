(window.webpackJsonp=window.webpackJsonp||[]).push([[6],{26:function(e,t,n){n.e(16).then((function(){var e=[n(0),n(214),n(215),n(19),n(18)];(function(e){"use strict";setInterval((function(){e("#mesz").load("refresh_time #time_table"),e("section.portletRecent").load("refresh_recent #recent_content")}),6e4);e(".documentByLine a").removeAttr("href").addClass("commentator");var t=e("#form-widgets-docType");if(null!=t[0]&&null!=t[0].selectedIndex){var n=function(e){var t="[?&]"+e+"=([^&]*)",n=location.search;if(e=new RegExp(t).exec(n))return e[1]}("form.widgets.docType:list");void 0!==n&&t.val(n);var o=t[0].options[t[0].selectedIndex].text,i=e("h1.documentFirstHeading").text();e("h1.documentFirstHeading").text(i+" ("+o+")")}e(document).ready((function(){e(".marquee").marquee({pauseOnHover:!0,duration:1e4,gap:50})}))}).apply(null,e)})).catch(n.oe),$(document).on("click",".collapsible",(function(e){this.classList.toggle("active");var t=this.nextElementSibling;t.style.maxHeight?t.style.maxHeight=null:t.style.maxHeight=t.scrollHeight+"px"}))}}]);