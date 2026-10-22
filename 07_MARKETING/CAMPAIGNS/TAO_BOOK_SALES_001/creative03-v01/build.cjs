const fs=require('fs');
const path=require('path');
const here=__dirname;
process.env.FONTCONFIG_FILE=path.join(here,'fonts.conf');
fs.writeFileSync(process.env.FONTCONFIG_FILE,`<?xml version="1.0"?><!DOCTYPE fontconfig SYSTEM "fonts.dtd"><fontconfig><dir>${here}/fonts</dir><cachedir>/private/tmp/tao-font-cache</cachedir></fontconfig>`);
const sharp=require('/Users/Drewdog19/.cache/codex-runtimes/codex-primary-runtime/dependencies/node/node_modules/sharp');
async function main(){
 const cover=await sharp(path.join(here,'PUBLISHED_COVER_FRONT_1800x2700.png')).resize(420,630,{kernel:'lanczos3'}).png().toBuffer();
 const b64=cover.toString('base64');
 const svg=`<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" width="1080" height="1350" viewBox="0 0 1080 1350">
 <defs><filter id="shadow" x="-35%" y="-20%" width="180%" height="160%"><feGaussianBlur stdDeviation="18"/></filter></defs>
 <rect width="1080" height="1350" fill="#F7F4EE"/>
 <g fill="#182633" font-family="Cormorant Garamond" font-weight="600" font-size="80">
 <text x="72" y="150">A PERSONAL TOUCH.</text><text x="72" y="231">FROM THE AUTHOR.</text></g>
 <g fill="#3A3A3A" font-family="Source Sans Pro" font-size="32"><text x="76" y="295">Personally inscribed and signed</text><text x="76" y="335">by Drew Freedman.</text></g>
 <rect x="341" y="410" width="420" height="630" fill="#182633" opacity=".18" filter="url(#shadow)"/>
 <image x="330" y="392" width="420" height="630" xlink:href="data:image/png;base64,${b64}"/>
 <text x="540" y="1101" text-anchor="middle" font-family="Source Sans Pro" font-weight="600" font-size="34" fill="#182633">$24.99 + $5 U.S. shipping</text>
 <text x="540" y="1141" text-anchor="middle" font-family="Source Sans Pro" font-size="25" fill="#3A3A3A">Tax calculated at checkout.</text>
 <line x1="72" y1="1237" x2="136" y2="1237" stroke="#B8860B" stroke-width="2"/>
 <text x="164" y="1249" font-family="Source Sans Pro" font-size="35" font-weight="600" fill="#182633">Make It Personal</text>
 </svg>`;
 fs.writeFileSync(path.join(here,'TAO_BOOK_SALES_001_CREATIVE03_FEED_1080x1350_v01_REVIEW.svg'),svg);
 const {createCanvas,GlobalFonts,loadImage}=require('/Users/Drewdog19/.cache/codex-runtimes/codex-primary-runtime/dependencies/node/node_modules/@napi-rs/canvas');
 GlobalFonts.registerFromPath(path.join(here,'fonts/CormorantGaramond.ttf'),'Cormorant Garamond');
 GlobalFonts.registerFromPath(path.join(here,'fonts/SourceSansPro-Regular.ttf'),'Source Sans Pro');
 GlobalFonts.registerFromPath(path.join(here,'fonts/SourceSansPro-Semibold.ttf'),'Source Sans Pro Semibold');
 const canvas=createCanvas(1080,1350),ctx=canvas.getContext('2d');
 ctx.fillStyle='#F7F4EE';ctx.fillRect(0,0,1080,1350);
 ctx.fillStyle='#182633';ctx.font='600 80px "Cormorant Garamond"';
 ctx.fillText('A PERSONAL TOUCH.',72,150);ctx.fillText('FROM THE AUTHOR.',72,231);
 ctx.fillStyle='#3A3A3A';ctx.font='32px "Source Sans Pro"';
 ctx.fillText('Personally inscribed and signed',76,295);ctx.fillText('by Drew Freedman.',76,335);
 ctx.save();ctx.shadowColor='rgba(24,38,51,0.20)';ctx.shadowBlur=30;ctx.shadowOffsetX=10;ctx.shadowOffsetY=18;
 ctx.drawImage(await loadImage(cover),330,392,420,630);ctx.restore();
 ctx.textAlign='center';ctx.fillStyle='#182633';ctx.font='34px "Source Sans Pro Semibold"';ctx.fillText('$24.99 + $5 U.S. shipping',540,1101);
 ctx.fillStyle='#3A3A3A';ctx.font='25px "Source Sans Pro"';ctx.fillText('Tax calculated at checkout.',540,1141);
 ctx.strokeStyle='#B8860B';ctx.lineWidth=2;ctx.beginPath();ctx.moveTo(72,1237);ctx.lineTo(136,1237);ctx.stroke();
 ctx.textAlign='left';ctx.fillStyle='#182633';ctx.font='35px "Source Sans Pro Semibold"';ctx.fillText('Make It Personal',164,1249);
 fs.writeFileSync(path.join(here,'TAO_BOOK_SALES_001_CREATIVE03_FEED_1080x1350_v01_REVIEW.png'),canvas.toBuffer('image/png'));
 console.log(await sharp(path.join(here,'TAO_BOOK_SALES_001_CREATIVE03_FEED_1080x1350_v01_REVIEW.png')).metadata());
}
main().catch(e=>{console.error(e);process.exit(1)});
