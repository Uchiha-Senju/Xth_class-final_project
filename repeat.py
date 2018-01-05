x = "     <div class=\"product-container\" onclick=\"window.open(\'\',\'_blank\')\">"
y = "      <img src=\"media/ram/%s.png\" alt=\"%s\">"
c = "      <div class=\"product_description\">"
a = "       <span class=\"price\">₹</span>"
d = "      </div>"
e = "     </div>"

for i in range(0,18):
 print(x)
 print(y % (i,i))
 print(c)
 print(a)
 print(d)
 print(e)
 
d = input("hello")
 