class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        D = {}
        for domain in cpdomains:
            count, site = domain.split(' ')
            # D[site]  = D.get(site,0) + int(count)
            subdomains = site.split('.')
            # print(subdomains)
            for i in range( len(subdomains) ):
                sub= '.'.join( subdomains[i:] )
                D[sub] =  D.get(sub,0) + int(count)
        print(D)
        answer = []
        for site, count in D.items():
            answer.append( str(count) +" " +site  )
        # print(answer)
        return answer
        