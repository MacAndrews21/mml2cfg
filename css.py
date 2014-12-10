try:
    import tinycss as ti
    print 'YEAH'
except:
    print 'nope'
    

css = ".roads-casing, .bridges-casing, .tunnels-casing { ::casing_links { [feature = 'highway_raceway'] { [zoom >= 14] { line-color: @secondary-casing; line-width: 6; line-join: round; } [zoom >= 16] { line-width: 8; } }"

stylesheet = ti.CSS21Parser().parse_stylesheet(css)
#print stylesheet.errors

#print decl.name for decl in stylesheet.rules[0].declarations


ti.parsing.validate_value(stylesheet)

#print style

  