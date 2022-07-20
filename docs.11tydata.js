let data = {
  layout: "docs/docpage.njk",
  tags: "docs",
};

// if(process.env.NODE_ENV === "production") {
data.date = "git Last Modified";
// }

module.exports = data;
