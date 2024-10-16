window.RevealRTD = window.RevealRTD || {
  id: 'rtd',
  init(reveal) {
    const deck = reveal;
    deck.addKeyBinding({keyCode: 68, key: 'D', description: 'Toggle RTD widget'}, function() {
      const flyout = document.querySelector("readthedocs-flyout");
      if (!flyout) return;
      flyout.style.display = flyout.style.display ? "" : "none";
    });
  }
}
