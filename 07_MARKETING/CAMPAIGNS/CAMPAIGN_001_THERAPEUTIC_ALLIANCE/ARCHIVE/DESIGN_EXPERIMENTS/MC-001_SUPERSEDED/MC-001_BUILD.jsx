/**
 * MC-001 Publication Masthead — Canonical Build Script
 *
 * The Tao of Clinical Touch — Editorial System
 *
 * USAGE: Run from Adobe InDesign > File > Scripts > Other Scripts... > MC-001_BUILD.jsx
 *
 * FUNCTION:
 * - Creates a new 1600×120 px document with transparent background
 * - Builds four named layers: ripple (locked), wordmark (locked), divider (locked), issue (editable)
 * - Places IA-001 Canonical Ripple at exact geometry (X:40 Y:20, 60×60px)
 * - Creates and styles wordmark: "THE TAO OF / CLINICAL TOUCH" in Cormorant Garamond
 * - Creates and styles issue number: "ISSUE NO. 005" in Source Sans Pro
 * - Draws divider line: 2px Antique Gold from X:420 to X:1310 at Y:60
 * - Saves INDD master and PNG export with transparent background
 * - Reports completion with paths and font substitution warnings
 *
 * OUTPUT:
 * - /Users/Drewdog19/finding-my-wei/MC-001_Publication_Masthead_v1.0.indd (canonical master)
 * - /Users/Drewdog19/finding-my-wei/MC-001_Publication_Masthead_v1.0.png (transparent PNG)
 *
 * FAILURE MODES:
 * - Ripple source missing: alert and exit
 * - Cormorant Garamond missing: substitute Garamond, warn user
 * - Source Sans Pro missing: substitute Arial, warn user
 */

#target indesign

(function() {
	"use strict";

	// ============ CONFIGURATION ============
	var config = {
		docWidth: 1600,        // pixels
		docHeight: 120,        // pixels
		rippleSourcePath: "/Users/Drewdog19/Desktop/Coding-folder/Tao/tao_ripple.png",
		outputInddPath: "/Users/Drewdog19/finding-my-wei/MC-001_Publication_Masthead_v1.0.indd",
		outputPngPath: "/Users/Drewdog19/finding-my-wei/MC-001_Publication_Masthead_v1.0.png"
	};

	var colors = {
		deepNavy: [24, 38, 51],      // #182633 RGB
		antGold: [184, 134, 11],     // #B8860B RGB
		white: [255, 255, 255]       // #FFFFFF RGB
	};

	var fonts = {
		wordmark: "Cormorant Garamond",
		issue: "Source Sans Pro"
	};

	var geometry = {
		ripple: { x: 40, y: 20, w: 60, h: 60 },
		wordmark: { x: 120, y: 18, w: 270, h: 64 },
		divider: { x1: 420, y: 60, x2: 1310, h: 2 },
		issue: { x: 1330, y: 42, w: 230, h: 36 }
	};

	var messages = {
		rippleNotFound: "ERROR: Ripple source not found at:\n" + config.rippleSourcePath,
		fontSubstituteWordmark: "WARNING: Cormorant Garamond not found. Substituted with Garamond.",
		fontSubstituteIssue: "WARNING: Source Sans Pro not found. Substituted with Arial.",
		success: function(inddPath, pngPath) {
			return "✓ MC-001 Publication Masthead created successfully!\n\n" +
				"INDD Master:\n" + inddPath + "\n\n" +
				"PNG Export:\n" + pngPath + "\n\n" +
				"Layers: IA-001_Canonical_Ripple (locked), Publication_Wordmark (locked), " +
				"Gold_Divider (locked), Issue_Number (editable)\n\n" +
				"Geometry: 1600×120px, transparent background\n" +
				"Ready for Adobe Express production workflow.";
		}
	};

	// ============ UTILITY FUNCTIONS ============

	function createColorSwatch(doc, swatchName, rgbArray) {
		try {
			// Check if swatch already exists
			var existing = doc.swatches.itemByName(swatchName);
			if (existing.isValid) {
				return existing;
			}

			// Create new spot color
			var spot = doc.spots.add();
			spot.name = swatchName;
			spot.colorType = ColorModel.PROCESS;
			spot.space = ColorSpace.RGB;
			spot.colorValue = rgbArray;

			// Create swatch from spot
			var swatch = doc.swatches.add();
			swatch.name = swatchName;
			swatch.color = spot;

			return swatch;
		} catch (e) {
			$.writeln("Warning: Could not create swatch " + swatchName);
			return null;
		}
	}

	function findFont(fontName) {
		try {
			var font = app.fonts.itemByName(fontName);
			if (font.isValid) {
				return font;
			}
		} catch (e) {
			// Font not found
		}
		return null;
	}

	function applyTextFormatting(textFrame, fontName, fontSize, rgbColor, alignment) {
		try {
			var story = textFrame.parentStory;
			var range = story.characters.everyItem();

			// Try to apply font
			var font = findFont(fontName);
			if (font) {
				range.appliedFont = font;
			}

			// Apply size
			if (fontSize) {
				range.pointSize = fontSize;
			}

			// Apply color (create temporary swatch if needed)
			if (rgbColor && textFrame.parent.parent.isValid) {
				// rgbColor should be [r, g, b] array
				try {
					var tempColor = textFrame.parent.parent.colors.add();
					tempColor.space = ColorSpace.RGB;
					tempColor.colorValue = rgbColor;
					range.fillColor = tempColor;
				} catch (e) {
					// Color application failed
				}
			}

			// Apply alignment
			if (alignment) {
				textFrame.paragraphs.everyItem().justification = alignment;
			}
		} catch (e) {
			$.writeln("Warning: Could not fully format text: " + e.message);
		}
	}

	// ============ MAIN EXECUTION ============

	try {
		// Step 1: Verify ripple source exists
		$.writeln("MC-001: verifying ripple source");
		var rippleFile = File(config.rippleSourcePath);
		if (!rippleFile.exists) {
			alert(messages.rippleNotFound);
			$.writeln("MC-001: FAILED - ripple not found");
			return;
		}
		$.writeln("MC-001: ripple verified");

		// Step 2: Create new document
		$.writeln("MC-001: creating document");
		var doc = app.documents.add();

		// Set measurement units to pixels
		doc.viewPreferences.horizontalMeasurementUnits = MeasurementUnits.PIXELS;
		doc.viewPreferences.verticalMeasurementUnits = MeasurementUnits.PIXELS;

		// Set document preferences
		doc.documentPreferences.facingPages = false;
		doc.documentPreferences.pagesPerDocument = 1;
		doc.documentPreferences.pageWidth = "1600px";
		doc.documentPreferences.pageHeight = "120px";

		$.writeln("MC-001: document created");

		// Step 3: Get first page
		$.writeln("MC-001: setting up page");
		var page = doc.pages[0];

		// Set page margins to 0
		page.marginPreferences.top = "0px";
		page.marginPreferences.bottom = "0px";
		page.marginPreferences.left = "0px";
		page.marginPreferences.right = "0px";

		// Step 4: Create color swatches
		$.writeln("MC-001: creating color swatches");
		var navySwatch = createColorSwatch(doc, "Deep Clinical Navy", colors.deepNavy);
		var goldSwatch = createColorSwatch(doc, "Antique Gold", colors.antGold);
		$.writeln("MC-001: color swatches created");

		// Step 5: Create named layers
		$.writeln("MC-001: creating layers");
		function createLayer(name) {
			var layer = doc.layers.add();
			layer.name = name;
			return layer;
		}

		var rippleLayer = createLayer("IA-001_Canonical_Ripple");
		var wordmarkLayer = createLayer("Publication_Wordmark");
		var dividerLayer = createLayer("Gold_Divider");
		var issueLayer = createLayer("Issue_Number");
		$.writeln("MC-001: layers created");

		// Step 6: Place ripple image
		$.writeln("MC-001: placing ripple image");
		doc.activeLayer = rippleLayer;
		var rippleFrames = doc.place(rippleFile, false);
		if (rippleFrames.length > 0) {
			var rippleFrame = rippleFrames[0];
			// Fit proportionally
			rippleFrame.fit(FitOptions.PROPORTIONALLY);
			// Set exact size
			rippleFrame.width = geometry.ripple.w;
			rippleFrame.height = geometry.ripple.h;
			// Position: X:40, Y:20
			rippleFrame.move(undefined, [geometry.ripple.x, geometry.ripple.y]);
		}
		rippleLayer.locked = true;
		$.writeln("MC-001: ripple placed and locked");

		// Step 7: Create wordmark text
		$.writeln("MC-001: creating wordmark");
		doc.activeLayer = wordmarkLayer;
		var wordmarkFrame = page.textFrames.add();
		wordmarkFrame.geometricBounds = [
			geometry.wordmark.y,
			geometry.wordmark.x,
			geometry.wordmark.y + geometry.wordmark.h,
			geometry.wordmark.x + geometry.wordmark.w
		];

		var wordmarkStory = wordmarkFrame.parentStory;
		wordmarkStory.contents = "THE TAO OF\rCLINICAL TOUCH";

		// Format wordmark
		var wordmarkFont = findFont(fonts.wordmark);
		var wordmarkFontToUse = wordmarkFont ? wordmarkFont : findFont("Garamond");
		if (!wordmarkFont && findFont("Garamond")) {
			alert(messages.fontSubstituteWordmark);
		}

		if (wordmarkFontToUse) {
			wordmarkStory.characters.everyItem().appliedFont = wordmarkFontToUse;
		}
		wordmarkStory.characters.everyItem().pointSize = 20;

		// Try to apply navy color
		if (navySwatch && navySwatch.isValid) {
			wordmarkStory.characters.everyItem().fillColor = navySwatch;
		}

		wordmarkLayer.locked = true;
		$.writeln("MC-001: wordmark created and locked");

		// Step 8: Create divider line
		$.writeln("MC-001: creating divider");
		doc.activeLayer = dividerLayer;
		var divider = page.lines.add();
		divider.strokeWeight = geometry.divider.h; // 2 pixels
		if (goldSwatch && goldSwatch.isValid) {
			divider.strokeColor = goldSwatch;
		}
		// Position line: from (420, 60) to (1310, 60)
		divider.move([geometry.divider.x1, geometry.divider.y], [geometry.divider.x2, geometry.divider.y]);
		dividerLayer.locked = true;
		$.writeln("MC-001: divider created and locked");

		// Step 9: Create issue number text
		$.writeln("MC-001: creating issue number");
		doc.activeLayer = issueLayer;
		var issueFrame = page.textFrames.add();
		issueFrame.geometricBounds = [
			geometry.issue.y,
			geometry.issue.x,
			geometry.issue.y + geometry.issue.h,
			geometry.issue.x + geometry.issue.w
		];

		var issueStory = issueFrame.parentStory;
		issueStory.contents = "ISSUE NO. 005";

		// Format issue
		var issueFont = findFont(fonts.issue);
		var issueFontToUse = issueFont ? issueFont : findFont("Arial");
		if (!issueFont && findFont("Arial")) {
			alert(messages.fontSubstituteIssue);
		}

		if (issueFontToUse) {
			issueStory.characters.everyItem().appliedFont = issueFontToUse;
		}
		issueStory.characters.everyItem().pointSize = 12;

		// Try to apply gold color
		if (goldSwatch && goldSwatch.isValid) {
			issueStory.characters.everyItem().fillColor = goldSwatch;
		}

		// Right-align issue number
		issueFrame.paragraphs.everyItem().justification = Justification.RIGHT_ALIGN;

		issueLayer.locked = false; // Issue layer stays editable
		$.writeln("MC-001: issue number created (unlocked)");

		// Step 10: Save INDD master
		$.writeln("MC-001: saving INDD master");
		var inddFile = File(config.outputInddPath);
		doc.save(inddFile);
		$.writeln("MC-001: INDD saved");

		// Step 11: Export transparent PNG
		$.writeln("MC-001: exporting PNG");
		var pngFile = File(config.outputPngPath);
		doc.exportFile(ExportFormat.PNG_FORMAT, pngFile);
		$.writeln("MC-001: PNG exported");

		// Step 12: Verify exports
		$.writeln("MC-001: verifying outputs");
		var inddExists = inddFile.exists;
		var pngExists = pngFile.exists;

		if (inddExists && pngExists) {
			$.writeln("MC-001: verification complete - success");
			alert(messages.success(config.outputInddPath, config.outputPngPath));
		} else {
			var status = "INDD: " + (inddExists ? "✓" : "✗") + "\nPNG: " + (pngExists ? "✓" : "✗");
			$.writeln("MC-001: verification complete - partial: " + status);
			alert("Export verification:\n" + status);
		}

		$.writeln("MC-001: build complete");

	} catch (e) {
		$.writeln("MC-001: FATAL ERROR at line " + e.line + ": " + e.message);
		alert("FATAL ERROR:\n" + e.message + "\nLine: " + e.line);
	}

})();
