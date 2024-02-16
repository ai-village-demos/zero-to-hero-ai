# Application Descriptions

## Amazon Analytics Website

### Describe the application to be modelled

    A web application that allows users to model pricing and inventory changes for their third party seller account at Amazon.com.
    The application is built on a Ruby on Rails backend with a MySQL database.
    Authentication is handled via the Devise Ruby authentication library.
    The frontend is built with HTML and CSS, using Bulma as its CSS library. Only vanilla JavaScript is used.
    Users can upload CSV or Excel files to import list of ISBNs, EANs, ASNs and other similar product codes.
    The product lists should only be accessible to users that are authorized on appropriate accounts.

### Application Properties

- Application type: Web Application
- Is the application internet-facing?: Yes
- What is the highest sensitivity level of the data processed by the application?: Unclassified
- What authentication methods are supported by the application?: Basic
- Are privileged accounts stored in a Privileged Access Management (PAM) solution?: No

## [Hyphanet](https://www.hyphanet.org/) (originally FreeNet)

### Describe the application to be modelled

    A fully distributed application that provides access to a new network as an overlay on top of the traditional internet.
    Users can create Free Sites (the equivalent of websites), browse newsgroups, and exchange files.
    Users access Hyphanet via a locally running proxy that connects to the distributed protocol and renders pages in a traditional web browser. Tor Browser is the recommended browser for Hyphanet.
    The protocol deamon and proxy are written in Java.
    This underlying protocol includes multiple security mitigations such as:
        - probablistic decrementing of TTLs to prevent TTL triangulation attacks
        - operation as an OpenNet or DarkNet node. In DarkNet mode connections are only made to nodes which the user has previously verified and directly exchanged strong cryptographic keys.
        - packets are forwarded with random delays to thwart timing attacks

### Application Properties

- Application type: Desktop Application
- Is the application internet-facing?: Yes
- What is the highest sensitivity level of the data processed by the application?: Unclassified
- What authentication methods are supported by the application?: None
- Are privileged accounts stored in a Privileged Access Management (PAM) solution?: No

### [Suntimes](https://github.com/forrestguice/SuntimesWidget)

Android app (and widget collection) that displays sunlight and moonlight times.

### Describe the application to be modelled

    An Android application written in Java that calculates the position of the Sun and Moon and various related times e.g. astronomical, nautical, civil, and actual sunrise and sunset.
    The app does not require GPS. The location is manually specified by default (and optionally obtained from GPS).
    The app does not require network connectivity (or other unnecessary permissions). All calculations are performed locally on the device.

### Application Properties

- Application type: Mobile Application
- Is the application internet-facing?: No
- What is the highest sensitivity level of the data processed by the application?: Unclassified
- What authentication methods are supported by the application?: None
- Are privileged accounts stored in a Privileged Access Management (PAM) solution?: No
