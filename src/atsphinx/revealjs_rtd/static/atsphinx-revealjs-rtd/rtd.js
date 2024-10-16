(function(g,f){typeof exports==='object'&&typeof module!=='undefined'?module.exports=f():typeof define==='function'&&define.amd?define(f):(g=typeof globalThis!=='undefined'?globalThis:g||self,g.RevealRTD=f());})(this,(function(){'use strict';const Plugin = {
  id: 'rtd',
  init(reveal) {
    const deck = reveal;
    deck.addKeyBinding({keyCode: 68, key: 'D', description: 'Toggle RTD widget'}, function() {
      console.debug("Press toggle-key of RTD.");
      const flyout = document.querySelector("readthedocs-flyout");
      if (!flyout) return;
      flyout.style.display = flyout.style.display ? "" : "none";
    });
  }
};

var plugin = () => Plugin;return plugin;}));