const esbuild = require("esbuild");
const { umdWrapper } = require("esbuild-plugin-umd-wrapper");

const baseDir = "src/atsphinx/revealjs_rtd/static/atsphinx-revealjs-rtd";

esbuild
  .build({
    entryPoints: [`${baseDir}/plugin.js`],
    outfile: `${baseDir}/rtd.js`,
    format: "umd",
    plugins: [umdWrapper({libraryName: "RevealRTD"})],
  })
  .then((result) => console.log(result))
  .catch(() => process.exit(1));
