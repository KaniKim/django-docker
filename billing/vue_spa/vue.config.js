const path = require("path");
module.exports = {
 publicPath: "/static/billing",
 outputDir: path.resolve(__dirname, "../static", "billing"),
 indexPath: path.resolve(__dirname, "../templates/", "billing",
 "index.html"),
};

