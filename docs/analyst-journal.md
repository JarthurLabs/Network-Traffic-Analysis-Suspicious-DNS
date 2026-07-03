# Analyst Journal

This project started with a suspicious DNS pattern, but the main lesson was restraint. Weird network traffic is worth investigating, but weird does not automatically mean malware.

## First pass

My first pass put too much weight on random-looking subdomains and NXDOMAIN responses. Those are useful clues, but by themselves they can also come from browser behavior, ad tech, misconfigured apps, telemetry, or normal software doing normal software things in the least elegant way possible.

## Correction

I changed the investigation to focus on correlation:

- same source workstation
- DNS burst
- multiple NXDOMAIN responses
- later HTTP requests to `/checkin`
- repeated pattern instead of one isolated packet

That made the case stronger without pretending the packet data proved malware.

## Threshold I reconsidered

I originally wanted to escalate based on DNS alone. That was too aggressive. The better threshold was DNS anomaly plus repeated outbound HTTP behavior from the same host.

Even then, the conclusion stays cautious: suspicious network activity requiring endpoint validation.

## Small lesson

Packets tell part of the story. Endpoint telemetry usually decides whether the story is actually scary or just another application making the network team sigh.