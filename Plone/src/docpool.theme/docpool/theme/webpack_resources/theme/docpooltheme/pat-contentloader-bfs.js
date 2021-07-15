(window["webpackJsonp"] = window["webpackJsonp"] || []).push([["pat-contentloader-bfs"],{

/***/ "./src/docpooltheme/pattern/pat-contentloader-bfs.js":
/*!***********************************************************!*\
  !*** ./src/docpooltheme/pattern/pat-contentloader-bfs.js ***!
  \***********************************************************/
/*! no static exports found */
/***/ (function(module, exports, __webpack_require__) {

eval("/* global require */\n// This is a custimized copy to contentloader mockup pattern.\n__webpack_require__.e(/*! AMD require */ 0).then(function() { var __WEBPACK_AMD_REQUIRE_ARRAY__ = [__webpack_require__(/*! jquery */ \"./.plone/++plone++static/components/jquery/dist/jquery.min.js\"), __webpack_require__(/*! pat-base */ \"./.plone/++plone++static/components/patternslib/src/core/base.js\"), __webpack_require__(/*! pat-logger */ \"./.plone/++plone++static/components/patternslib/src/core/logger.js\"), __webpack_require__(/*! pat-registry */ \"./.plone/++plone++static/components/patternslib/src/core/registry.js\"), __webpack_require__(/*! mockup-utils */ \"./.plone/++resource++mockupjs/utils.js\"), __webpack_require__(/*! underscore */ \"./.plone/++plone++static/components/underscore/underscore.js\")]; (function ($, Base, logger, Registry, utils, _) {\n  'use strict';\n\n  var log = logger.getLogger('pat-contentloader-bfs');\n  var ContentLoader = Base.extend({\n    name: 'contentloader-bfs',\n    trigger: '.pat-contentloader-bfs',\n    parser: 'mockup',\n    defaults: {\n      url: null,\n      content: null,\n      trigger: 'click',\n      target: null,\n      template: null,\n      dataType: 'html'\n    },\n    init: function init() {\n      var that = this;\n\n      if (that.options.url === 'el' && that.$el[0].tagName === 'A') {\n        that.options.url = that.$el.attr('href');\n      }\n\n      that.$el.removeClass('loading-content');\n      that.$el.removeClass('content-load-error');\n\n      if (that.options.trigger === 'immediate') {\n        that._load();\n      } else {\n        that.$el.on(that.options.trigger, function (e) {\n          e.preventDefault();\n\n          that._load();\n        });\n      }\n    },\n    _load: function _load() {\n      var that = this;\n      that.$el.addClass('loading-content');\n      that.$el.toggleClass('close'); // State :)\n\n      var $metadata = false;\n      var $metatitle = false; // Is the other meta column open? If close it\n\n      var other_column = that.$el.parent().find('a').not('.loading-content');\n\n      if (other_column != that.$el) {\n        if (other_column.hasClass('close')) {\n          other_column.removeClass('close');\n        }\n      }\n\n      var $already_open = that.$el.closest('tr').next('tr');\n\n      if ($already_open.hasClass('target_open')) {\n        $already_open.remove();\n      } else {\n        if (that.options.url) {\n          // Load Metadata\n          that.loadRemote();\n        } else {\n          // Load Metatitle\n          that.loadLocal();\n        }\n      }\n    },\n    loadRemote: function loadRemote() {\n      var that = this;\n      $.ajax({\n        url: that.options.url,\n        dataType: that.options.dataType,\n        success: function success(data) {\n          var $el;\n\n          if (that.options.dataType === 'html') {\n            if (data.indexOf('<html') !== -1) {\n              data = utils.parseBodyTag(data);\n            }\n\n            $el = $('<tr class=\"target_open\"><td>&nbsp</td><td>&nbsp</td> <td>&nbsp</td><td colspan=\"3\">' + data + '</td> <td>&nbsp</td> <td>&nbsp</td></tr>'); // jQuery starts to search at the first child element.\n          } else if (that.options.dataType.indexOf('json') !== -1) {\n            // must have template defined with json\n            if (data.constructor === Array && data.length === 1) {\n              // normalize json if it makes sense since some json returns as array with one item\n              data = data[0];\n            }\n\n            try {\n              $el = $(_.template(that.options.template)(data));\n            } catch (e) {\n              that.$el.removeClass('loading-content');\n              that.$el.addClass('content-load-error');\n              log.warn('error rendering template. pat-contentloader will not work');\n              return;\n            }\n          }\n\n          if (that.options.content !== null) {\n            $el = $el.find(that.options.content);\n          }\n\n          that.loadLocal($el);\n        },\n        error: function error() {\n          that.$el.removeClass('loading-content');\n          that.$el.addClass('content-load-error');\n        }\n      });\n    },\n    loadLocal: function loadLocal($content) {\n      var that = this;\n\n      if (!$content && that.options.content === null) {\n        that.$el.removeClass('loading-content');\n        that.$el.addClass('content-load-error');\n        log.warn('No selector configured');\n        return;\n      }\n\n      var $target = that.$el;\n\n      if (that.options.target !== null) {\n        $target = $(that.options.target);\n\n        if ($target.size() === 0) {\n          that.$el.removeClass('loading-content');\n          that.$el.addClass('content-load-error');\n          log.warn('No target nodes found');\n          return;\n        }\n      }\n\n      if (!$content) {\n        var $content_raw = $(that.options.content).clone();\n        $content = $('<tr class=\"target_open\"><td>&nbsp</td><td>&nbsp</td> <td>&nbsp</td><td colspan=\"3\"><h4>' + $content_raw.text() + '</h4></td> <td>&nbsp</td> <td>&nbsp</td></tr>'); // jQuery starts to search at the first child element.\n      }\n\n      $target = $target.closest('tr');\n\n      if ($content.length) {\n        $content.show();\n        $target.after($content);\n        Registry.scan($content);\n      } else {\n        // empty target node instead of removing it.\n        // allows for subsequent content loader calls to work sucessfully.\n        $target.empty();\n      }\n\n      that.$el.removeClass('loading-content');\n      that.emit('loading-done');\n    }\n  });\n  return ContentLoader;\n}).apply(null, __WEBPACK_AMD_REQUIRE_ARRAY__);}).catch(__webpack_require__.oe);\n\n//# sourceURL=webpack:///./src/docpooltheme/pattern/pat-contentloader-bfs.js?");

/***/ })

}]);