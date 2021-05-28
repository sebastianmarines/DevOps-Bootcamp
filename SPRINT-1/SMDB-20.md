# S3

AWS Simple Storage Service is a object storage service with a durability of 99.99999999999%.

It allows you to upload files up to 5 TB, and this files are stored in containers called buckets.

An object consists of data, a key (this is the name of the object), and metadata.

## Storage levels
- Standard frequent access
- Intelligent tiering: This option allows you to save money by automatically moving objects across tiers.
- Infrequent access: It has a minimum storage duration and gives access to the requested object in miliseconds and the objects can be stored on multiple availability zones.
- One zone IA: This level is similar to the _One zone IA_ but the objects can only be stored in one availability zone.
- S3 Glacier: This storage class is meant for data archiving which could be accessed from minutes to hours and would be accessed rarely.
- S3 Glacier Deep Archive: This level is for data that will be accessed once or twice a year. It is designed to retain data for 10 years or longer to meet compliance requirements.
