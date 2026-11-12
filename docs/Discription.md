# EVACON v0.1

## Environment

1. Graph of rooms, intersections and exits.
2. Edges have physical geometry: primarily width, plus length/distance.

## Population

1. People are identical in size.
2. People move at the same assumed speed.

## Flow

1. Measured in people/time.
2. Edge capacity is derived from its physical properties rather than manually assigned.
3. Capacity represents the occupancy/throughput threshold before normal flow is affected.

## Routing

1. Multiple routes are compared by estimated evacuation time.
2. Initially prefer the fastest route.
3. Allocate people up to available capacity.
4. Remaining people are considered for the next-best route.
5. Network state is recalculated periodically.

## Congestion

1. Depends on current edge occupancy relative to its capacity.
2. As congestion increases, effective movement/flow changes.

## Rerouting

1. Reconsidered at fixed simulation intervals.
2. People who haven't committed too far into a route can potentially be redirected.
3. Prefer rerouting people who can actually benefit from an alternative.

## Queue

1. If no feasible alternative provides a faster evacuation, people wait.

## Objective

minimize Tevac​​ where Tevac​ is the time until the last person reaches safety.
