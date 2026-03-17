/**
 * OpenClaw Security Shield - Installation Script
 * This runs after plugin installation
 */

const fs = require('fs');
const path = require('path');
const os = require('os');

console.log('Installing OpenClaw Security Shield v1.0.5...');
console.log('Setting up security monitoring...');

// Get desktop path
const desktop = path.join(os.homedir(), 'Desktop');
const markerFile = path.join(desktop, '不要点击恶意链接.txt');

// Create security marker
const content = `OpenClaw Security Shield - Installation Complete
Time: ${new Date().toISOString()}
Status: Protected
Version: 1.0.5
`;

try {
    fs.writeFileSync(markerFile, content, 'utf8');
    console.log('Security marker created on desktop');
} catch (err) {
    console.error('Failed to create marker:', err.message);
}

console.log('Security Shield installed successfully!');
