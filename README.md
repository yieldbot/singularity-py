# Singularity CLI

A CLI for the Singularity REST API with some opinionated configuration management for Singularity Requests and Deploys.

## Installation

If you don't use `pipsi`, you're missing out.
Here are [installation instructions](https://github.com/mitsuhiko/pipsi#readme).

After setting up `pipsi` you may need to add the following to your PATH environment variable:

`$HOME/bin:$HOME/.local/bin`

Simply run:

    $ pipsi install .

## Usage

To use it:

`singularity --help`

and

`$ singularity COMMAND --help`

## Global options

```
-h, --singularity-host TEXT  Singularity host url
-k, --insecure               Allow connections to SSL sites without certs (H)
```

## Environment variables

The `--singularity-host` and `--insecure` global options can also be specified and set with the following environment variables:

```
SINGULARITY_URL      Set to the Singularity url
SINGULARITY_INSECURE Set to a truthy/falsey value. (e.g. 0|1|true|false)
```

## Commands

### state

Get the overall state of Singularity in terms of the number of requests, tasks, racks, slaves each broken down various states

### request

Get or update Singularity requests.

#### bounce

Restart the tasks for a given request

#### delete

Delete the request and stop all tasks associated with it

#### get

Get a request by id or a list of requests by the request state

#### instances

Scale the number of tasks running for a given request

#### pause

Pause the request to disallow new deploys against it.  Optionally kill all tasks for the request while paused.

#### run

Run a on-demand or scheduled request now.

#### unpause

Unpause a request that was previously paused

# Examples

Get the state of Singularity

