const http = require('node:http');
const name = '${{ values.component_id }}';
http.createServer((req,res)=>{ res.writeHead(req.url === '/health' ? 200 : 200, {'content-type':'text/plain'}); res.end(req.url === '/health' ? 'ok' : `hello from ${name}`); }).listen(8080,'0.0.0.0');
