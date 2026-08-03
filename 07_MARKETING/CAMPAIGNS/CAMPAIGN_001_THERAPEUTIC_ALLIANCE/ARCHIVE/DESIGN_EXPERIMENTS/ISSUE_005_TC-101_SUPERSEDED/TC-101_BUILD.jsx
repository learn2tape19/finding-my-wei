/**
 * TC-101 Laura Boozer Testimonial — Instagram Portrait Foundation Proof
 *
 * The Tao of Clinical Touch — Testimonial Design System
 *
 * USAGE: Run from Adobe InDesign > File > Scripts > Other Scripts... > TC-101_BUILD.jsx
 *
 * FUNCTION:
 * - Creates 1080 × 1350 px document (Instagram Portrait)
 * - Builds 9 named layers with intentional lock states
 * - Places Laura Boozer documentary photograph with controlled geometry
 * - Creates editorial thesis: "CLINICAL PRECISION NEEDS THE RIGHT CONDITIONS."
 * - Creates verified quotation in warm-ivory card with gold divider
 * - Creates verified attribution: LAURA BOOZER / LMT, BCTMB, AUTHOR
 * - Places canonical ripple and Tao brand signature
 * - Adds CTA: AVAILABLE NOW ON AMAZON
 * - Exports clean JPG proof at exact 1080×1350px
 * - Saves INDD master
 *
 * OUTPUT:
 * - /Users/Drewdog19/finding-my-wei/TC-101_Laura_Boozer_Instagram_Portrait_v1.0.indd
 * - /Users/Drewdog19/finding-my-wei/TC-101_Laura_Boozer_Instagram_Portrait_v1.0.jpg
 */

#target indesign

(function() {
	"use strict";

	// ============ CONFIGURATION ============
	var config = {
		docWidth: 1080,
		docHeight: 1350,
		photoSourcePath: "/Users/Drewdog19/Desktop/Coding-folder/Tao/Laura Boozer_Tao Review.jpg",
		rippleSourcePath: "/Users/Drewdog19/Desktop/Coding-folder/Tao/tao_ripple.png",
		outputInddPath: "/Users/Drewdog19/finding-my-wei/TC-101_Laura_Boozer_Instagram_Portrait_v1.0.indd",
		outputJpgPath: "/Users/Drewdog19/finding-my-wei/TC-101_Laura_Boozer_Instagram_Portrait_v1.0.jpg"
	};

	var colors = {
		midnightNavy: [15, 27, 45],
		deepNavy: [24, 38, 51],
		antiquGold: [201, 164, 106],
		warmIvory: [243, 239, 230],
		charcoal: [26, 26, 26]
	};

	var fonts = {
		serif: [
			"Cormorant Garamond\tRegular",
			"Adobe Garamond Pro\tRegular",
			"Garamond\tRegular",
			"Times New Roman\tRegular"
		],
		sans: [
			"Source Sans Pro\tRegular",
			"Source Sans 3\tRegular",
			"Arial\tRegular",
			"Helvetica\tRegular"
		]
	};

	var copy = {
		thesis: "CLINICAL PRECISION NEEDS THE RIGHT CONDITIONS.",
		quotation: "What I love most is that it doesn't ask you to abandon clinical precision. It builds the conditions where that precision can finally work.",
		attribution1: "LAURA BOOZER",
		attribution2: "LMT, BCTMB, AUTHOR",
		tagline: "BETTER CONNECTION. BETTER CARE. BETTER OUTCOMES.",
		cta: "AVAILABLE NOW ON AMAZON"
	};

	var messages = {
		photoNotFound: "ERROR: Laura photo not found at:\n" + config.photoSourcePath,
		rippleNotFound: "ERROR: Canonical ripple not found at:\n" + config.rippleSourcePath,
		fontMissing: function(fontName) {
			return "WARNING: " + fontName + " not found. Substituted with approved alternative.";
		},
		success: function(inddPath, jpgPath) {
			return "✓ TC-101 Laura Boozer Foundation Proof created!\n\n" +
				"INDD Master:\n" + inddPath + "\n\n" +
				"JPG Proof (1080×1350px):\n" + jpgPath + "\n\n" +
				"Layers: 9 (Background, Photo, Thesis, Quote, Attribution, Ripple, Signature, CTA, Guides)\n" +
				"Geometry: 1080×1350px, RGB, 72 PPI\n" +
				"Next: Open in InDesign, run preflight, review before Founder acceptance.";
		}
	};

	// ============ UTILITY FUNCTIONS ============

	function createColorSwatch(doc, swatchName, rgbArray) {
		try {
			var existing = doc.colors.itemByName(swatchName);
			if (existing.isValid) {
				return existing;
			}
			return doc.colors.add({
				name: swatchName,
				model: ColorModel.PROCESS,
				space: ColorSpace.RGB,
				colorValue: rgbArray
			});
		} catch (e) {
			$.writeln("Warning: Could not create color " + swatchName);
			return null;
		}
	}

	function findInstalledFont(fontNames) {
		for (var i = 0; i < fontNames.length; i++) {
			try {
				var font = app.fonts.itemByName(fontNames[i]);
				if (
					font.isValid &&
					font.status === FontStatus.INSTALLED
				) {
					$.writeln("Using installed font: " + fontNames[i]);
					return font;
				}
			} catch (e) {
				$.writeln("Unavailable font: " + fontNames[i]);
			}
		}
		$.writeln("No requested font available; retaining InDesign default.");
		return null;
	}

	function applyFontSafely(textObject, font) {
		if (!font) {
			return false;
		}
		try {
			textObject.appliedFont = font;
			return true;
		} catch (e) {
			$.writeln(
				"Font assignment skipped: " +
				font.name +
				" — " +
				e.message
			);
			return false;
		}
	}

	// ============ MAIN EXECUTION ============

	try {
		// Step 1: Verify assets
		$.writeln("TC-101: verifying assets");
		var photoFile = File(config.photoSourcePath);
		var rippleFile = File(config.rippleSourcePath);

		if (!photoFile.exists) {
			alert(messages.photoNotFound);
			$.writeln("TC-101: FAILED - photo not found");
			return;
		}
		if (!rippleFile.exists) {
			alert(messages.rippleNotFound);
			$.writeln("TC-101: FAILED - ripple not found");
			return;
		}
		$.writeln("TC-101: assets verified");

		// Step 2: Create document
		$.writeln("TC-101: creating document");
		var doc = app.documents.add();

		doc.viewPreferences.horizontalMeasurementUnits = MeasurementUnits.PIXELS;
		doc.viewPreferences.verticalMeasurementUnits = MeasurementUnits.PIXELS;

		doc.documentPreferences.facingPages = false;
		doc.documentPreferences.pagesPerDocument = 1;
		doc.documentPreferences.pageWidth = "1080px";
		doc.documentPreferences.pageHeight = "1350px";

		var page = doc.pages[0];
		page.marginPreferences.top = "0px";
		page.marginPreferences.bottom = "0px";
		page.marginPreferences.left = "0px";
		page.marginPreferences.right = "0px";

		$.writeln("TC-101: document created (1080×1350px)");

		// Step 3: Create color swatches
		$.writeln("TC-101: creating color swatches");
		var navySwatch = createColorSwatch(doc, "Midnight Navy", colors.midnightNavy);
		var deepNavySwatch = createColorSwatch(doc, "Deep Navy", colors.deepNavy);
		var goldSwatch = createColorSwatch(doc, "Antique Gold", colors.antiquGold);
		var ivorySwatch = createColorSwatch(doc, "Warm Ivory", colors.warmIvory);
		var charcoalSwatch = createColorSwatch(doc, "Charcoal", colors.charcoal);
		var noneSwatch = doc.swatches.itemByName("None");
		$.writeln("TC-101: color swatches created");

		// Step 4: Create named layers (reuse Layer 1, then add 8 more = 9 total)
		$.writeln("TC-101: creating layers");
		var bgLayer = doc.layers[0];
		bgLayer.name = "Background_LOCKED";

		function createLayer(name) {
			var layer = doc.layers.add();
			layer.name = name;
			return layer;
		}

		var photoLayer = createLayer("Documentary_Photo_EDITABLE");
		var thesisLayer = createLayer("Editorial_Thesis_EDITABLE");
		var quoteLayer = createLayer("Verified_Quote_EDITABLE");
		var attrLayer = createLayer("Verified_Attribution_EDITABLE");
		var rippleLayer = createLayer("Canonical_Ripple_LOCKED");
		var sigLayer = createLayer("Brand_Signature_LOCKED");
		var ctaLayer = createLayer("CTA_EDITABLE");
		var guideLayer = createLayer("Guides_NONPRINTING");
		guideLayer.printable = false;

		$.writeln("TC-101: layers created (9 total)");

		// Step 5: Background
		$.writeln("TC-101: setting background");
		doc.activeLayer = bgLayer;
		var bgRect = page.rectangles.add();
		bgRect.geometricBounds = [0, 0, config.docHeight, config.docWidth];
		if (navySwatch && navySwatch.isValid) {
			bgRect.fillColor = navySwatch;
		}
		bgRect.strokeColor = noneSwatch;
		bgLayer.locked = true;

		// Step 6: Place photograph with controlled frame geometry
		$.writeln("TC-101: placing photograph");
		doc.activeLayer = photoLayer;
		var photoFrame = page.rectangles.add();
		photoFrame.itemLayer = photoLayer;
		photoFrame.geometricBounds = [80, 40, 520, 420];
		photoFrame.strokeColor = noneSwatch;
		photoFrame.place(photoFile);
		photoFrame.fit(FitOptions.FILL_PROPORTIONALLY);
		photoFrame.fit(FitOptions.CENTER_CONTENT);
		$.writeln("TC-101: photograph placed");

		// Step 7: Editorial Thesis
		$.writeln("TC-101: creating thesis");
		doc.activeLayer = thesisLayer;
		var thesisFrame = page.textFrames.add();
		thesisFrame.geometricBounds = [100, 450, 280, 1040];
		var thesisStory = thesisFrame.parentStory;
		thesisStory.contents = copy.thesis;

		var thesisFont = findInstalledFont(fonts.serif);
		applyFontSafely(
			thesisStory.characters.everyItem(),
			thesisFont
		);
		thesisStory.characters.everyItem().pointSize = 22;
		if (ivorySwatch && ivorySwatch.isValid) {
			thesisStory.characters.everyItem().fillColor = ivorySwatch;
		}
		$.writeln("TC-101: thesis created");

		// Step 8: Verified Quotation Card
		$.writeln("TC-101: creating quotation card");
		doc.activeLayer = quoteLayer;

		var quoteCardBg = page.rectangles.add();
		quoteCardBg.geometricBounds = [350, 60, 950, 1020];
		if (ivorySwatch && ivorySwatch.isValid) {
			quoteCardBg.fillColor = ivorySwatch;
		}
		quoteCardBg.strokeColor = noneSwatch;

		var quoteFrame = page.textFrames.add();
		quoteFrame.geometricBounds = [380, 110, 800, 990];
		var quoteStory = quoteFrame.parentStory;
		quoteStory.contents = "“" + copy.quotation + "”";

		var quoteFont = findInstalledFont(fonts.serif);
		applyFontSafely(
			quoteStory.characters.everyItem(),
			quoteFont
		);
		quoteStory.characters.everyItem().pointSize = 18;
		if (charcoalSwatch && charcoalSwatch.isValid) {
			quoteStory.characters.everyItem().fillColor = charcoalSwatch;
		quoteStory.paragraphs.everyItem().justification = Justification.CENTER_ALIGN;
		quoteStory.paragraphs.everyItem().leading = 24;
		}
		$.writeln("TC-101: quotation created");

		// Step 9: Verified Attribution
		$.writeln("TC-101: creating attribution");
		doc.activeLayer = attrLayer;

		var divider = page.graphicLines.add();
		divider.geometricBounds = [905, 90, 905, 990];
		if (goldSwatch && goldSwatch.isValid) {
			divider.strokeColor = goldSwatch;
		}
		divider.strokeWeight = 1;
		divider.itemLayer = attrLayer;

		var attrFrame = page.textFrames.add();
		attrFrame.geometricBounds = [915, 90, 948, 990];
		var attrStory = attrFrame.parentStory;
		attrStory.contents = copy.attribution1 + "\n" + copy.attribution2;

		var attrFont = findInstalledFont(fonts.sans);
		applyFontSafely(
			attrStory.characters.everyItem(),
			attrFont
		);
		attrStory.characters.everyItem().pointSize = 11;
		if (deepNavySwatch && deepNavySwatch.isValid) {
			attrStory.characters.everyItem().fillColor = deepNavySwatch;
		attrStory.paragraphs.everyItem().justification = Justification.CENTER_ALIGN;
		}
		$.writeln("TC-101: attribution created");

		// Step 10: Canonical Ripple with controlled frame
		$.writeln("TC-101: placing ripple");
		doc.activeLayer = rippleLayer;
		var rippleFrame = page.rectangles.add();
		rippleFrame.itemLayer = rippleLayer;
		rippleFrame.geometricBounds = [980, 80, 1060, 160];
		rippleFrame.strokeColor = noneSwatch;
		rippleFrame.place(rippleFile);
		rippleFrame.fit(FitOptions.PROPORTIONALLY);
		rippleFrame.fit(FitOptions.CENTER_CONTENT);
		rippleLayer.locked = true;
		$.writeln("TC-101: ripple placed and locked");

		// Step 11: Brand Signature
		$.writeln("TC-101: creating brand signature");
		doc.activeLayer = sigLayer;

		var sigFrame = page.textFrames.add();
		sigFrame.geometricBounds = [1000, 200, 1080, 1000];
		var sigStory = sigFrame.parentStory;
		sigStory.contents = "THE TAO OF CLINICAL TOUCH\n\n" + copy.tagline;

		var sigFont = findInstalledFont(fonts.serif);
		applyFontSafely(
			sigStory.characters.everyItem(),
			sigFont
		);
		sigStory.characters.everyItem().pointSize = 12;
		if (ivorySwatch && ivorySwatch.isValid) {
			sigStory.characters.everyItem().fillColor = ivorySwatch;
		}
		sigLayer.locked = true;
		$.writeln("TC-101: brand signature created");

		// Step 12: CTA
		$.writeln("TC-101: creating CTA");
		doc.activeLayer = ctaLayer;

		var ctaRule = page.graphicLines.add();
		ctaRule.geometricBounds = [1100, 200, 1100, 1000];
		if (goldSwatch && goldSwatch.isValid) {
			ctaRule.strokeColor = goldSwatch;
		}

		var ctaFrame = page.textFrames.add();
		ctaFrame.geometricBounds = [1120, 200, 1340, 1000];
		var ctaStory = ctaFrame.parentStory;
		ctaStory.contents = copy.cta;

		var ctaFont = findInstalledFont(fonts.sans);
		applyFontSafely(
			ctaStory.characters.everyItem(),
			ctaFont
		);
		ctaStory.characters.everyItem().pointSize = 10;
		if (ivorySwatch && ivorySwatch.isValid) {
			ctaStory.characters.everyItem().fillColor = ivorySwatch;
		ctaStory.paragraphs.everyItem().justification = Justification.CENTER_ALIGN;
		}
		$.writeln("TC-101: CTA created");

		// Step 13: Save INDD master
		$.writeln("TC-101: saving INDD master");
		var inddFile = File(config.outputInddPath);
		doc.save(inddFile);
		$.writeln("TC-101: INDD saved");

		// Step 14: Configure JPG export for exact pixel dimensions
		$.writeln("TC-101: configuring JPG export");
		var jpgSettings = doc.jpegExportPreferences;
		jpgSettings.jpegQuality = JPEGOptionsQuality.MAXIMUM;
		jpgSettings.jpegExportRange = ExportRangeOrAllPages.EXPORT_ALL;
		jpgSettings.exportResolution = 72;
		jpgSettings.jpegColorSpace = JpegColorSpaceEnum.RGB;
		jpgSettings.antiAlias = true;
		jpgSettings.useDocumentBleeds = false;
		jpgSettings.exportingSpread = false;

		// Step 15: Export JPG proof
		$.writeln("TC-101: exporting JPG proof at 1080×1350px");
		var jpgFile = File(config.outputJpgPath);
		doc.exportFile(ExportFormat.JPG, jpgFile);
		$.writeln("TC-101: JPG exported");

		// Step 16: Verify outputs
		$.writeln("TC-101: verifying outputs");
		var inddExists = inddFile.exists;
		var jpgExists = jpgFile.exists;

		if (inddExists && jpgExists) {
			$.writeln("TC-101: verification complete - success");
			alert(messages.success(config.outputInddPath, config.outputJpgPath));
		} else {
			var status = "INDD: " + (inddExists ? "✓" : "✗") + "\nJPG: " + (jpgExists ? "✓" : "✗");
			$.writeln("TC-101: verification complete - partial");
			alert("Export verification:\n" + status);
		}

		$.writeln("TC-101: build complete");

	} catch (e) {
		$.writeln("TC-101: FATAL ERROR at line " + e.line + ": " + e.message);
		alert("FATAL ERROR:\n" + e.message + "\nLine: " + e.line);
	}

})();
