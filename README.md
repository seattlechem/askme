# askme
## [askm3.com](https://0bfdff96.ngrok.io/)

**Authors**:
- [Peter Kim](https://github.com/seattlechem)
- [Andrii Glukhyi](https://github.com/andriiglukhyi)
- [Ramon Mendoza](https://github.com/brickfaced)

**Version**: 1.0.0

[![Build Status](https://travis-ci.org/seattlechem/askme.svg?branch=master)](https://travis-ci.org/seattlechem/askme) [![Coverage Status](https://coveralls.io/repos/github/seattlechem/askme/badge.svg)](https://coveralls.io/github/seattlechem/askme)

## API
<!-- Provide detailed instructions for your applications usage. This should include any methods or endpoints available to the user/client/developer. Each section should be formatted to provide clear syntax for usage, example calls including input data requirements and options, and example responses or return values. -->

#### api/v1/ask
- Sends binary audio file and recieves back text representation of answer

### api/v1/audio
- Sends binary audio file and recieves back binary audio file of the answer

#### Wolfram Alpha
- Accepts questions as queries and responds with answers as text.
#### Google Speech API
- Used to translate Wolfram Alpha answers into a speech to give that feeling of conversation to our user.

## Change Log
<!-- Use this are to document the iterative changes made to your application as each feature is successfully implemented. Use time stamps. Here's an example:

01-01-2001 4:59pm - Added functionality to add and delete some things.
-->
| Date | |
|:--|:--|
| 5-25-2018 | Final Presentation |
| 5-24-2018 | Testing complete |
| 5-23-2018 | Started working on voice logic |
| 5-22-2018 | Initial setup, install Django, complete rest api |

## Resources
- gitignore.io
- editorconfig.org
- github.com/necolas/normalize.css
- github.com/jiaaro/pydub/
- github.com/pygame/pygame
- github.com/jrief/django-sass-processor
- github.com/voxy/django-audio-recorder

![](assets/data_flow.jpeg)
