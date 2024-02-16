## Threat Model

| Threat Type | Scenario | Potential Impact |
|-------------|----------|------------------|
| Spoofing | An attacker might spoof the GPS signal to manipulate the app into calculating incorrect positions of the Sun and Moon when the user opts to use GPS data. | This could result in misleading information being presented to the user, potentially affecting activities that rely on accurate solar/lunar positions. |
| Tampering | Given that the app does not require network connectivity, an attacker could tamper with the app’s local storage or its codebase if they gain physical access to the device. | Altered calculations or functionality may mislead users or cause the app to malfunction. |
| Repudiation | Without any authentication or logging mechanism, it’s impossible to trace and verify user actions within the app, such as changes to location settings or other configurations. | Issues or disputes regarding unauthorized changes in the app’s settings cannot be resolved due to lack of auditing capabilities. |
| Information Disclosure | If the device is compromised, an attacker could access stored location data entered by the user, even though it is classified as unclassified. | Revealing users' manually entered locations could lead to privacy violations, especially if the locations are sensitive or personal. |
| Denial of Service | An attacker with physical or malware-based access to the device might overload the app with invalid data inputs, such as nonsensical location coordinates, causing it to crash or become unresponsive. | Users would be unable to access the app's functionalities, affecting their ability to calculate the positions of the Sun and Moon. |
| Elevation of Privilege | An attacker may exploit a vulnerability within the app, potentially gaining elevated privileges on the device, especially if the app is granted unnecessary permissions by the user. | This could lead to unauthorized actions being performed on the device, compromising its security and the data it contains. |


## Improvement Suggestions

- Implement an authentication mechanism to ensure that users are accountable for actions taken within the app.
- Include a feature for logging user actions within the app to enable audit trails and support repudiation controls.
- Ensure that the application requests only the minimum necessary permissions to reduce the risk of privilege escalation attacks.
- Consider encrypting sensitive data, such as saved locations, to protect against information disclosure if the device is compromised.
- Perform regular security assessments to identify and mitigate vulnerabilities that could be exploited for tampering or elevation of privilege.
