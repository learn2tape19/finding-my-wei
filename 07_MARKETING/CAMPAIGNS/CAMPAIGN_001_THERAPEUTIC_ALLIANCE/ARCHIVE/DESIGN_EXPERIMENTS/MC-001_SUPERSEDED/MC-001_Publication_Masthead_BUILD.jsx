/**
 * MC-001 Publication Masthead Build Script
 *
 * Constructs the canonical masthead for The Tao of Clinical Touch
 * Document: 1600 × 120 px, transparent background, RGB
 *
 * Usage: Run in Adobe InDesign via File > Scripts > Other Scripts... > MC-001_Publication_Masthead_BUILD.jsx
 *
 * Output:
 * - MC-001_Publication_Masthead_v1.0.indd (canonical master)
 * - MC-001_Publication_Masthead_v1.0.png (transparent export)
 *
 * Geometry (in pixels):
 * - Ripple: X 40, Y 20, W 60, H 60 (locked)
 * - Wordmark frame: X 120, Y 18, W 270, H 64 (locked)
 * - Divider: X 420 to X 1310, Y 60, 2px (locked)
 * - Issue frame: X 1330, Y 42, W 230, H 36 (editable)
 * - Right margin: 40px
 */

#target indesign

try {
	// Configuration
	var rippleSourcePath = "/Users/Drewdog19/Desktop/Coding-folder/Tao/tao_ripple.png";
	var outputPath = "/Users/Drewdog19/finding-my-wei/MC-001_Publication_Masthead_v1.0.indd";
	var exportPath = "/Users/Drewdog19/finding-my-wei/MC-001_Publication_Masthead_v1.0.png";

	var colors = {
		deepNavy: "#182633",
		antGold: "#B8860B",
		white: "#FFFFFF"
	};

	var fonts = {
		wordmark: "Cormorant Garamond",
		issue: "Source Sans Pro"
	};

	// Step 1: Verify ripple source exists
	var rippleFile = File(rippleSourcePath);
	if (!rippleFile.exists) {
		alert("ERROR: Ripple source not found at " + rippleSourcePath);
		exit();
	}

	// Step 2: Create new document (1600×120 px)
	var docPreset = app.documents.documentPresets.itemByName("Custom");
	if (docPreset == null) {
		docPreset = app.documents.documentPresets[0];
	}

	var doc = app.documents.add(false, docPreset);

	// Set page size to 1600×120 px (convert to points: 1px = 0.75pt at 72dpi)
	// Actually, InDesign works in points, but we can set in different units
	var page = doc.pages[0];

	// Set document to 1600×120 px
	page.pageWidth = "1600px";
	page.pageHeight = "120px";

	// Set background to transparent (no fill)
	page.fillColor = "None";

	// Step 3: Create color swatches
	function createSwatch(swatchName, hexColor) {
		var swatch;
		try {
			swatch = doc.swatches.itemByName(swatchName);
			if (swatch.length == 0) {
				swatch = doc.spots.add();
				swatch.name = swatchName;

				var color = doc.colors.add();
				color.name = swatchName;
				color.colorType = ColorModel.PROCESS;
				color.space = ColorSpace.RGB;

				// Convert hex to RGB
				var rgb = hexToRgb(hexColor);
				color.colorValue = [rgb.r, rgb.g, rgb.b];

				swatch = doc.swatches.add();
				swatch.name = swatchName;
				swatch.color = color;
			}
		} catch (e) {
			// Swatch creation may fail; try direct color assignment later
		}
		return swatch;
	}

	function hexToRgb(hex) {
		// Remove # and parse
		var hex = hex.replace("#", "");
		return {
			r: parseInt(hex.substring(0, 2), 16) / 255 * 100,
			g: parseInt(hex.substring(2, 4), 16) / 255 * 100,
			b: parseInt(hex.substring(4, 6), 16) / 255 * 100
		};
	}

	// Create color swatches
	var navySwatch = createSwatch("Deep Clinical Navy", colors.deepNavy);
	var goldSwatch = createSwatch("Antique Gold", colors.antGold);

	// Step 4: Create named layers
	function createLayer(layerName, locked) {
		var layer = doc.layers.add();
		layer.name = layerName;
		if (locked !== false) {
			layer.locked = false; // Start unlocked for construction
		}
		return layer;
	}

	var rippleLayer = createLayer("IA-001_Canonical_Ripple");
	var wordmarkLayer = createLayer("Publication_Wordmark");
	var dividerLayer = createLayer("Gold_Divider");
	var issueLayer = createLayer("Issue_Number", false);

	// Step 5: Place ripple image on rippleLayer
	doc.activeLayer = rippleLayer;
	var rippleFrame = doc.place(rippleFile, false);
	rippleFrame[0].fit(FitOptions.PROPORTIONALLY);
	rippleFrame[0].width = "60px";
	rippleFrame[0].height = "60px";
	rippleFrame[0].move(undefined, [40, 20]);

	// Step 6: Add wordmark text on wordmarkLayer
	doc.activeLayer = wordmarkLayer;
	var wordmarkFrame = page.textFrames.add();
	wordmarkFrame.geometricBounds = [18, 120, 82, 390]; // [top, left, bottom, right] in pixels

	var wordmarkStory = wordmarkFrame.parentStory;
	wordmarkStory.contents = "THE TAO OF\rCLINICAL TOUCH";

	// Format wordmark text
	var wordmarkRange = wordmarkStory.paragraphs[0].characters;
	wordmarkRange.appliedFont = doc.fonts.itemByName(fonts.wordmark);
	if (wordmarkRange.appliedFont.length == 0) {
		// Font not found, try alternative
		wordmarkRange.appliedFont = doc.fonts.itemByName("Garamond");
		alert("WARNING: Cormorant Garamond not found, substituted with Garamond");
	}
	wordmarkRange.pointSize = 20;
	wordmarkRange.fillColor = navySwatch.length > 0 ? navySwatch : doc.swatches.itemByName("Black");

	// Step 7: Add divider line on dividerLayer (X 420 to X 1310, Y 60, 2px)
	doc.activeLayer = dividerLayer;
	var divider = page.lines.add();
	divider.strokeWeight = "2px";
	divider.strokeColor = goldSwatch.length > 0 ? goldSwatch : doc.swatches.itemByName("Black");
	divider.move([420, 60], [1310, 60]);

	// Step 8: Add issue number text on issueLayer (editable)
	doc.activeLayer = issueLayer;
	var issueFrame = page.textFrames.add();
	issueFrame.geometricBounds = [42, 1330, 78, 1560]; // [top, left, bottom, right]

	var issueStory = issueFrame.parentStory;
	issueStory.contents = "ISSUE NO. 005";

	// Format issue text
	var issueRange = issueStory.paragraphs[0].characters;
	issueRange.appliedFont = doc.fonts.itemByName(fonts.issue);
	if (issueRange.appliedFont.length == 0) {
		// Font not found, try alternative
		issueRange.appliedFont = doc.fonts.itemByName("Arial");
		alert("WARNING: Source Sans Pro not found, substituted with Arial");
	}
	issueRange.pointSize = 12;
	issueRange.fillColor = goldSwatch.length > 0 ? goldSwatch : doc.swatches.itemByName("Black");

	// Align issue text to the right
	issueFrame.paragraphStyleRange.justification = Justification.RIGHT_ALIGN;

	// Step 9: Lock immutable layers
	rippleLayer.locked = true;
	wordmarkLayer.locked = true;
	dividerLayer.locked = true;
	issueLayer.locked = false; // Issue number layer remains editable

	// Step 10: Save INDD master
	var inddFile = File(outputPath);
	doc.save(inddFile);
	alert("✓ INDD master saved: " + outputPath);

	// Step 11: Export transparent PNG
	var pngFile = File(exportPath);

	// Set up export settings
	var exportSettings = doc.pngExportPreferences;
	exportSettings.antiAlias = true;
	exportSettings.transparency = true;
	exportSettings.resolution = 300; // DPI for export

	// Export PNG
	doc.export(ExportFormat.PNG_FORMAT, pngFile);
	alert("✓ PNG export saved: " + exportPath);

	// Step 12: Verify export
	if (pngFile.exists) {
		alert("✓ PNG export verified");
		$.writeln("MC-001 build complete. Output files:");
		$.writeln("  INDD: " + outputPath);
		$.writeln("  PNG:  " + exportPath);
	} else {
		alert("ERROR: PNG export verification failed");
	}

	// Summary
	var summary = "MC-001 Publication Masthead created successfully.\n\n";
	summary += "Geometry:\n";
	summary += "  Document: 1600×120px, transparent\n";
	summary += "  Ripple: X40, Y20, 60×60px (locked)\n";
	summary += "  Wordmark: X120, Y18, 270×64px (locked)\n";
	summary += "  Divider: X420-X1310, Y60, 2px (locked)\n";
	summary += "  Issue: X1330, Y42, 230×36px (editable)\n\n";
	summary += "Output files:\n";
	summary += "  INDD: " + outputPath + "\n";
	summary += "  PNG: " + exportPath + "\n\n";
	summary += "Fonts: Cormorant Garamond (wordmark), Source Sans Pro (issue)\n";
	summary += "Colors: Deep Clinical Navy (#182633), Antique Gold (#B8860B)\n";

	alert(summary);

} catch (e) {
	alert("FATAL ERROR: " + e.message + "\nLine: " + e.line);
	$.writeln("Error: " + e.message);
}
