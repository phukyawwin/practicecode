#split out the letters and numbers from string
select project,
       regexp_replace(address, '[[:digit:]]', '', 'g') as letters,
       regexp_replace(address, '[[:alpha:]]', '', 'g') as numbers
from repositories;