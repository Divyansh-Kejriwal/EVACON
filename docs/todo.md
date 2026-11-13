# EVACON — TODO

## Current Phase: Graph Representation

### 1. Verify Graph Representation

- ✔ Confirm `Graph`, `nodes`, and `edges` work correctly.
- ✔ Test that nodes can be retrieved using their IDs.
- ✔ Test that edge information can be accessed:
- ✔ Start node
- ✔ End node
- ✔ Distance
- ✔ Width
- ✔ Make `show()` output readable enough to inspect the graph.

### 2. Decide Graph Design

- [ ] Decide whether edges should be directed or undirected.
- [ ] Decide how connected nodes will be found from the graph.
- [ ] Keep physical properties separate from routing calculations.

### 3. Build the First Routing Algorithm

- [ ] Define what "best route" means for the first version.
- [ ] Implement Dijkstra's algorithm.
- [ ] Test Dijkstra on the small manual evacuation network.
- [ ] Verify that the algorithm can find a route from a room to an exit.
- [ ] Test multiple possible routes and compare their costs.

### 4. Connect Routing to EVACON

- [ ] Determine how edge distance becomes travel time.
- [ ] Determine how edge width will eventually affect movement/flow.
- [ ] Keep these calculations separate from the basic graph structure.

---

## After Basic Routing Works

### 5. Introduce Population

- [ ] Add multiple rooms with different populations.
- [ ] Calculate evacuation routes for each population source.
- [ ] Determine total evacuation time.

### 6. Introduce Capacity and Flow

- [ ] Define how corridor width determines capacity.
- [ ] Define normal flow rate.
- [ ] Model people entering and leaving an edge.
- [ ] Track the number of people currently occupying each edge.

### 7. Introduce Congestion

- [ ] Define when congestion begins.
- [ ] Make flow rate change with current edge occupancy.
- [ ] Calculate the resulting increase in travel/evacuation time.

### 8. Introduce Dynamic Rerouting

- [ ] Detect when an edge becomes inefficient/congested.
- [ ] Check available alternative routes.
- [ ] Compare estimated evacuation times.
- [ ] Reroute eligible people when an alternative is faster.
- [ ] Queue people when no better route exists.

### 9. Build the Evacuation Simulation

- [ ] Introduce fixed simulation time steps.
- [ ] Update people positions.
- [ ] Update edge occupancy.
- [ ] Recalculate flow/congestion.
- [ ] Re-evaluate route choices.
- [ ] Continue until everyone reaches an exit.

### 10. Analysis

- [ ] Calculate total evacuation time.
- [ ] Identify bottlenecks.
- [ ] Compare routing strategies.
- [ ] Test different population distributions.
- [ ] Test different exit configurations.
- [ ] Test blocked/failed corridors.
- [ ] Evaluate network resilience.

### 11. Visualization

- [ ] Visualize the graph.
- [ ] Visualize population distribution.
- [ ] Visualize routes.
- [ ] Visualize congestion.
- [ ] Visualize evacuation over time.
- [ ] Visualize final bottlenecks and results.

---

## Important Rule

Do not implement everything at once.

Current target:

Graph → verify → routing → verify → population → capacity → congestion → rerouting → simulation → analysis

Each stage should work before adding the next one.
