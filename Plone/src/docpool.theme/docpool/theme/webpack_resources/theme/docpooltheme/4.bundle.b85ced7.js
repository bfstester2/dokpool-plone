(window.webpackJsonp=window.webpackJsonp||[]).push([[4],{82:function(t,n){function o(){var t=$("link[rel='canonical']").attr("href")+"/@@json_collections_count";$.getJSON(t,(function(t){if(t.criterionId){var n=t.criterionId;t.countByCollection.forEach((function(t){$("li#"+n+t.uid+" .term-count").html(t.count)}))}}))}function c(){$.getJSON($("body").data("portalUrl")+"/@@json_list_countable_tabs",(function(t){t.urls.forEach((function(t){$.get(t+"/@@json_collections_count",(function(n){var o=JSON.parse(n),c=$("#portal-globalnav a[href='"+t+"']"),e=0;o.countByCollection.forEach((function(t){e+=parseInt(t.count)}));var i=c.html(),a=i.match(/^(.+) \(\d+\)$/);a&&(i=a[1]);var l=i+" ("+e+")";c.html(l)}))}))}))}$(document).ready((function(){$('div[class*="faceted-tagscloud-collection-widget"').length>0&&(null===sessionStorage.getItem("tabs_count_timeout")&&(sessionStorage.setItem("tabs_count_timeout","0"),c()),Boolean($("div#faceted-form").length)||o(),$(Faceted.Events).bind(Faceted.Events.AJAX_QUERY_SUCCESS,(function(){o()})),$("body").on("click","#collections-count-refresh",(function(){c()}))),Faceted.Options.FADE_SPEED=0}))}}]);