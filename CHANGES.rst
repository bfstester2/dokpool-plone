Changelog
=========

1.8.4 (04.11.2021)
------------------

Technical:

- Remove remnants of old testdata infrastructure to simplify buildout #4405
  [tlotze]

- Update Version of plone.session (#4539)
  [tlotze]


Fixed:

- Fix initialising scenarios when adding a document w.r.t. inactive ones (#4527)
  [tlotze]

- Prevent KeyError when no DPEvent for a scenario can be found (#4504)
  [pbauer, slindner]

- Fix deleteTransferDataInDB (#4117)
  [pbauer]

- Fix UnicodeDecodeError when filtering in @@rpopup (#4507)
  [pbauer]


1.8.3 (29.09.2021)
------------------

Technical:

- Configured 4 additional instances, changed varnish timeouts #4475
  [slindner, tlotze, kprobst]
    - Configured 4 additional instances, changed varnish timeouts #4475 [slindner, tlotze, kprobst]


1.8.2 (12.08.2021)
------------------

Added:

- Add js alert to confirm bulk transitions #4396
  [pbauer]


Changed:

- Use dview if the parent is a collection #4392
  [pbauer]


Fixed:

- Fix year filter - facetednavigation #4394
  [slindner]

- Remove unallowed value from OriginVocabulary #4388
  [pbauer]

- Disable broken sorting in faceted navigation results table #4395
  [pbauer]

- Fix no_value option in AutoritiesVocabulary #4418
  [pbauer]


1.8.1 (19.07.2021)
------------------

Fixed:

- Fix logic for deselecting scenarios #4324
  [tlotze, pbauer]


1.8.0 (19.07.2021)
------------------

Added:

- Added faceted navigation functionality in REI: facetednavigation-webpack #2634
  [slindner]

- Added bulk actions: bulk transfer #2693, bulk actions in collections #3460
  [pbauer]


Changed:

- Added Collection to allowed content types for Simplefolder #4342
  [pbauer]

- Require medium for REI-E reports #4269
  [pbauer]

- Removed milliseconds in portlet recent in ELAN
  [kprobst]


Fixed:

- Fixed unicode indexes in REI #4084
  [pbauer]

- Fixed creating events without journals in ELAN #4267
  [pbauer]

- Fixed bug in creating new DocTypes #4266
  [tlotze]

- Fixed sorting in REI AuthorityVocabulary #4336
  [pbauer]

- Deactivate checkboxes when de/selecting events #4078
  [tlotze]


Technical:

- Fix zcml: Drop obsolete explicit zcml-slugs. Only use those with i18n-override #4349
  [pbauer]


1.7.4 (10.06.2021)
------------------

Fixed:

- Update Products.PloneHotfix20210518 and allow text/html to be displayed inline
  [pbauer]


1.7.3 (25.05.2021)
------------------

Fixed:

- Bump last weeks hotfix 20210518 to version 1.2
  [tlotze]

- Deployed on master as hotfix
  [kprobst]


1.7.2 (22.05.2021)
------------------

Fixed:

- Add Plone hotfix 20210518
  [tlotze]

- Deployed on master as hotfix
  [kprobst]


1.7.1 (23.03.2021)
------------------

Changed:

- Switched to new CI runner & docker #4158
  [slindner]

- Simplify generated title for REI-reports. #4224
  [kprobst]


1.7.0 (12.02.2021)
------------------

Added:

- Added Changelog
  [slindner]

- Add custom add-form for DPDocument to hide title-field for reireport #4039
  [pbauer]

- Add automatic transfer of published documents to other docpools. #2601
  [tlotze]


Changed:

- Close all popups on logout #3512
  [slindner]

- Do not display content of text files #4038
  [pbauer]


Fixed:

- Fix Unicode Errors in AUTHORITYS vocabulary and use ISO values #3953
  [slindner]

- Fix compatability mode in Internet Explorer #3991
  [slindner]

- Fix editing help page and move it to each docpool #2439
  [tlotze]

- Only use global imprint, fix actions and views for help and imprint, move
  these texts out of contentconfig folders #4067
  [tlotze]

- Add hotfix to fix canchangepassword #4085
  Deployed on master as hotfix.
  [kprobst]


Technical:

- Remove the concept and implementation of auditing #3954
  [tlotze]

- Remove elan.irix and all other IRIX-related code #3954
  [tlotze]

- Remove archetypes dependencies #3225
  [tlotze]
