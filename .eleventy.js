const { EleventyHtmlBasePlugin } = require("@11ty/eleventy");

module.exports = function (eleventyConfig) {

	eleventyConfig.addPlugin(EleventyHtmlBasePlugin);
	eleventyConfig.addPassthroughCopy("./src/assets/");
	eleventyConfig.addPassthroughCopy("./src/css/");
	eleventyConfig.addWatchTarget("./src/css/");	

	return {
		pathPrefix: "/CGNotes/",
		htmlTemplateEngine: "njk",
		dir: {
			input: "src",
			output: "public"
		}
	};
};