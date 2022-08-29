let data = {
  layout: "docs/docpage.njk",
  tags: "docs",
  sitemapchangefrequency: "daily",
  sitemappriority: "0.7",
};

// if(process.env.NODE_ENV === "production") {
data.date = "git Last Modified";
// }

module.exports = data;
