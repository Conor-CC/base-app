# base-app

This Django Application is envisioned as being a WIP highly configurable, secure and efficient means of managing the following...

- Multiple Kinds of User Model (inheriting from a base)
- Authentication (With the planned option for configuration of preferred protocols such as Token, JWT, OAuth2 etc.)
- Generic email notifications for user signups, interactions etc.
- REST API for portabilty
- Modelling of very abstract interactions to enable this app to easily plug in to e-commerce scenarios. Such scenarios include Multi-Vendor marketplaces, Booking management, Buying of Services etc. (this is one of the most challenging tasks!)

And all of this using modern and up-to-date django with as little reliance on third-party packages as possible (to reduce headache caused by obsolete or unmaintained apps). This is as much a learning experience for me as it could also be a very useful tool in the future for rapid implementations of MVPs.
