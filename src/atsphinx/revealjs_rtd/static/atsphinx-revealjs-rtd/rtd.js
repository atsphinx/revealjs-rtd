(function(g,f){if(typeof exports=="object"&&typeof module<"u"){module.exports=f()}else if("function"==typeof define && define.amd){define("RevealRTD",f)}else {g["RevealRTD"]=f()}}(typeof globalThis < "u" ? globalThis : typeof self < "u" ? self : this,function(){var exports={};var __exports=exports;var module={exports};
var __defProp = Object.defineProperty;
var __getOwnPropDesc = Object.getOwnPropertyDescriptor;
var __getOwnPropNames = Object.getOwnPropertyNames;
var __hasOwnProp = Object.prototype.hasOwnProperty;
var __export = (target, all) => {
  for (var name in all)
    __defProp(target, name, { get: all[name], enumerable: true });
};
var __copyProps = (to, from, except, desc) => {
  if (from && typeof from === "object" || typeof from === "function") {
    for (let key of __getOwnPropNames(from))
      if (!__hasOwnProp.call(to, key) && key !== except)
        __defProp(to, key, { get: () => from[key], enumerable: !(desc = __getOwnPropDesc(from, key)) || desc.enumerable });
  }
  return to;
};
var __toCommonJS = (mod) => __copyProps(__defProp({}, "__esModule", { value: true }), mod);
var plugin_exports = {};
__export(plugin_exports, {
  default: () => plugin_default
});
module.exports = __toCommonJS(plugin_exports);
const Plugin = {
  id: "rtd",
  init(reveal) {
    const deck = reveal;
    deck.addKeyBinding({ keyCode: 68, key: "D", description: "Toggle RTD widget" }, function() {
      const flyout = document.querySelector("readthedocs-flyout");
      if (!flyout) return;
      flyout.style.display = flyout.style.display ? "" : "none";
    });
  }
};
var plugin_default = () => Plugin;

if(__exports != exports)module.exports = exports;return module.exports}));
