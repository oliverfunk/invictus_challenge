# Invictus Coding Challenge

## Setup

Build the docker image:

```bash
docker build --tag inv_nameko_service .
```

Create a docker network. This will allow the `inv_nameko_service` container to connect to the RabbitMQ service container:

```bash
docker network create inv_test_net
```

Start a RabbitMQ docker container with the name `rabbitmq_ser`, using the `inv_test_net` network:

```bash
docker run -d --rm --name rabbitmq_ser --net inv_test_net -p 5672:5672 rabbitmq:3
```

Start the `inv_nameko_service` docker container, also using the `inv_test_net` network:

```bash
docker run -d --rm --name inv_nameko_service --net inv_test_net inv_nameko_service
```

If all has gone well the `inv_nameko_service` should be up and connected to the RabbitMQ service.

Now start a bash session inside the `inv_nameko_service` container:

```bash
docker exec -it inv_nameko_service bash
```

And start a `nakemo shell` session inside the container, with the correct configuration:

```bash
nameko shell --config conf.yml
```

The `conf.yml` file defines the AMQI API endpoint used by Nakemo.

## Usage

Three RPC methods can be called within a `nameko shell` connected to the `inv_nameko_service`.

### Square each odd number

The `square_odds` function accepts a list of integers and will return the list with each the square of each odd number.

An error will be thrown if the input is not a list of int's.

For example:

```python
n.rpc.inv_nameko_service.square_odds([1,2,3,4,5,6,7,8,9,10])
# [1, 2, 9, 4, 25, 6, 49, 8, 81, 10]
```

### Compress list of strings

The `compress_list_map` function accepts a list of `UTF-8` encoded strings and returns a `Dict` with the key being the original string and the value being a lossless compressed version of that string, in hex format.

The compression is doing using the python `zlib` built-in library.

An error will be thrown if the input is not a list of strings

For example:

```python
n.rpc.inv_nameko_service.compress_list_map(["a reptetive reptetive reptetive reptetive reptetive reptetive reptetive reptetive reptetive string", "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Donec laoreet neque ligula, sed rhoncus lacus tempus id. Maecenas mattis vestibulum nunc, ut porttitor lacus. Morbi eros magna, placerat a odio at, mollis luctus justo. Sed condimentum odio a aliquet congue. Proin eu imperdiet lectus, et euismod massa. Proin consectetur facilisis tempor. Sed rhoncus nulla ac justo finibus egestas. Maecenas ultricies convallis metus at rhoncus. Nullam nec blandit purus. Donec vel ligula egestas, tempus est a, vestibulum quam. Nulla molestie mattis suscipit. Lorem ipsum dolor sit amet, consectetur adipiscing elit. Maecenas nec tristique purus, et porta est. Proin id lacus feugiat, faucibus lectus non, gravida lorem. Maecenas sit amet facilisis elit."])
# {'a reptetive reptetive reptetive reptetive reptetive reptetive reptetive reptetive reptetive string': '789c4b54284a2d28492dc92c4ba53aabb8a428332f1d00779026d1', 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Donec laoreet neque ligula, sed rhoncus lacus tempus id. Maecenas mattis vestibulum nunc, ut porttitor lacus. Morbi eros magna, placerat a odio at, mollis luctus justo. Sed condimentum odio a aliquet congue. Proin eu imperdiet lectus, et euismod massa. Proin consectetur facilisis tempor. Sed rhoncus nulla ac justo finibus egestas. Maecenas ultricies convallis metus at rhoncus. Nullam nec blandit purus. Donec vel ligula egestas, tempus est a, vestibulum quam. Nulla molestie mattis suscipit. Lorem ipsum dolor sit amet, consectetur adipiscing elit. Maecenas nec tristique purus, et porta est. Proin id lacus feugiat, faucibus lectus non, gravida lorem. Maecenas sit amet facilisis elit.': '789c9d52498edc300cfc0a1f60f815739c0401e6056c89ed30a0248f44f6fb53b2db81cfb9780197daf8d9ba14d27d44a1dcac751aeac4457ca1d4ea90e4e2d189b3ee3a92d68dc4d457fa68551219635e9caa7c8790e916c60b0dc9d47fb79a62a0633e5dca8e97e6957eb024a93ca8b0bb0e7ac9707d8481408d9a160aa7bd75d41c6c8e710cb5fe5092dee6d85681b1a3229dc1955ad6460cc2a59961a3457280fd89e16da52f908192ac45aa03e4ec263605659fa52d64a55fbd692509d2b24bcf8a92c9dcb3103e25749496013e065fcd777f9e9c14d87a4a6dfdc4bd4ca86106c87472a2a756281e241bb4f3b87912e65d93ca98cb5f7cc84116e885d2f7b6957ece75b00b013c8c210d8e459f95339597d83b8b0b62b912c01fc1bd9be9dfc1e5bd721a380b7265330291ef33eecfffbd937fd2263188c3fa792a07dfc3da99354f5e97ad9adf47f394d874e6fae44887616722545b5d68ebfcd2cc6493d90de7e2758be460f217ebac11b1'}
```

### Decompress previously compressed string

The `decompress_string` function accepts a string that was previously compressed (in hex format) and return the decompressed original `UTF-8` string.

An error is thrown if the input is not a string and if the string is not hex formatted.

For example:

```python
n.rpc.inv_nameko_service.decompress_string("789c9d52498edc300cfc0a1f60f815739c0401e6056c89ed30a0248f44f6fb53b2db81cfb9780197daf8d9ba14d27d44a1dcac751aeac4457ca1d4ea90e4e2d189b3ee3a92d68dc4d457fa68551219635e9caa7c8790e916c60b0dc9d47fb79a62a0633e5dca8e97e6957eb024a93ca8b0bb0e7ac9707d8481408d9a160aa7bd75d41c6c8e710cb5fe5092dee6d85681b1a3229dc1955ad6460cc2a59961a3457280fd89e16da52f908192ac45aa03e4ec263605659fa52d64a55fbd692509d2b24bcf8a92c9dcb3103e25749496013e065fcd777f9e9c14d87a4a6dfdc4bd4ca86106c87472a2a756281e241bb4f3b87912e65d93ca98cb5f7cc84116e885d2f7b6957ece75b00b013c8c210d8e459f95339597d83b8b0b62b912c01fc1bd9be9dfc1e5bd721a380b7265330291ef33eecfffbd937fd2263188c3fa792a07dfc3da99354f5e97ad9adf47f394d874e6fae44887616722545b5d68ebfcd2cc6493d90de7e2758be460f217ebac11b1")
# 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Donec laoreet neque ligula, sed rhoncus lacus tempus id. Maecenas mattis vestibulum nunc, ut porttitor lacus. Morbi eros magna, placerat a odio at, mollis luctus justo. Sed condimentum odio a aliquet congue. Proin eu imperdiet lectus, et euismod massa. Proin consectetur facilisis tempor. Sed rhoncus nulla ac justo finibus egestas. Maecenas ultricies convallis metus at rhoncus. Nullam nec blandit purus. Donec vel ligula egestas, tempus est a, vestibulum quam. Nulla molestie mattis suscipit. Lorem ipsum dolor sit amet, consectetur adipiscing elit. Maecenas nec tristique purus, et porta est. Proin id lacus feugiat, faucibus lectus non, gravida lorem. Maecenas sit amet facilisis elit.'
```

## Technical review

### Nameko

The Nameko library provided a framework for writing microservices, using RabbitMQ (an AMQP messaging protocol service) to do RPC.

The microservices architecture improves the maintainability of a system by, for example, allowing new versions of the service to be rolled out safely (by, for example, incrementally increasing traffic to the new version). Importantly, because microservices are written without dependencies on other services, they can be tested easily.

The Nameko library was easy to use and provided great tooling for testing the service. Nameko does seem quite coupled to RabbitMQ. If another messaging service was being used, it may be more difficult to integrate Nameko with it.

### Docker

Docker was used to containerise the Nameko service, bundling its dependencies into an easy to run image.

### Compression using zlib

The built-in standard python compression library zlib was chosen for the string compression task. zlib uses the DEFLATE algorithm for lossless compression, which uses a combination of the LZSS algorithm and Huffman coding.

The zlib library provides a convenient compression/decompression API, which is fast, configurable and can handle large input strings. When used on large input data strings (say base64 encoded images) it can provide compression ratios of between 50% to 25%. It was chosen for these reasons and because it is very well known and well tested. One downside of using zlib is for the smaller test inputs used, the compression can be quite bad or even worse (more data) than the input due to headers being needed.

The following compression ratios were achieved for the tested strings:

- 55% reduction for the repetitive string
- 98% for the lorem string
