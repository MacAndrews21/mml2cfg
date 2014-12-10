.roads-casing, .bridges-casing, .tunnels-casing {
  ::casing_links {
    [feature = 'highway_raceway'] {
      [zoom >= 14] {
        line-color: @secondary-casing;
        line-width: 6;
        line-join: round;
      }
      [zoom >= 16] { line-width: 8; }
    }