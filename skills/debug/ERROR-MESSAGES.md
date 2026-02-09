# Common Error Messages

What errors mean and how to fix them.

---

## JavaScript Errors

### "Cannot read property 'X' of undefined"

**What it means:**
Trying to access property of something that doesn't exist.

**Example:**
```javascript
user.profile.name  // Error if user.profile is undefined
```

**Common causes:**
- Data not loaded yet
- API returned null
- Typo in property name
- Wrong data structure

**Fix:**
```
Add checks before accessing:
- if (user?.profile?.name)
- Optional chaining (?.)
- Load data before rendering
```

### "Cannot read property 'X' of null"

**What it means:**
Similar to undefined, but explicitly null.

**Common causes:**
- Database returned null
- User not found
- Data deleted
- Form field empty

**Fix:**
```
Check for null before using:
- if (data !== null)
- Provide default values
- Handle empty states
```

### "Maximum call stack size exceeded"

**What it means:**
Infinite loop or recursion.

**Common causes:**
- Function calls itself forever
- Circular reference
- State update triggers itself

**Fix:**
```
Find the loop:
- Check recursive functions
- Check useEffect dependencies
- Check state update logic
- Add base case to recursion
```

### "Unexpected token"

**What it means:**
Syntax error in code.

**Common causes:**
- Missing comma or bracket
- Typo in code
- Wrong quotes
- Copy-paste error

**Fix:**
```
Check syntax:
- Match all brackets { [ (
- Check commas in objects/arrays
- Verify quotes match
- Use linter/formatter
```

---

## Network Errors

### "Failed to fetch" / "Network request failed"

**What it means:**
Couldn't connect to API.

**Common causes:**
- No internet connection
- API server down
- CORS issue
- Wrong URL

**Fix:**
```
Check:
- Is API running?
- Is URL correct?
- Is CORS configured?
- Add error handling for offline
```

### "401 Unauthorized"

**What it means:**
Not authenticated.

**Common causes:**
- Not logged in
- Token expired
- Token invalid
- Wrong token sent

**Fix:**
```
Check authentication:
- Is user logged in?
- Is token in request?
- Is token expired?
- Redirect to login if needed
```

### "403 Forbidden"

**What it means:**
Authenticated but not allowed.

**Common causes:**
- Wrong permissions
- Try to access other user's data
- Try to access admin route
- Account suspended

**Fix:**
```
Check authorization:
- Does user have permission?
- Check user role
- Check resource ownership
- Show proper error message
```

### "404 Not Found"

**What it means:**
Resource doesn't exist.

**Common causes:**
- Wrong URL
- Item deleted
- ID doesn't exist
- Route not defined

**Fix:**
```
Handle gracefully:
- Show "Not found" page
- Check if URL correct
- Verify ID exists
- Redirect to valid page
```

### "429 Too Many Requests"

**What it means:**
Rate limit exceeded.

**Common causes:**
- Too many API calls
- Rapid clicking
- No debouncing
- Loop making requests

**Fix:**
```
Reduce requests:
- Add debouncing
- Disable button after click
- Cache responses
- Batch requests
- Wait before retry
```

### "500 Internal Server Error"

**What it means:**
Server crashed or has bug.

**Common causes:**
- Backend code error
- Database connection lost
- Uncaught exception
- Resource exhausted

**Fix:**
```
Check server:
- Look at server logs
- Check recent deploys
- Verify database connection
- Check resource usage
- Rollback if needed
```

### "502 Bad Gateway" / "503 Service Unavailable"

**What it means:**
Service temporarily down.

**Common causes:**
- Server restarting
- Deployment happening
- Too much traffic
- Database down

**Fix:**
```
Usually temporary:
- Wait and retry
- Check hosting status
- Check if deploying
- Scale up if needed
```

### "504 Gateway Timeout"

**What it means:**
Request took too long.

**Common causes:**
- Slow database query
- Slow external API
- Processing too much data
- Server overloaded

**Fix:**
```
Speed up request:
- Optimize queries
- Add timeout handling
- Process asynchronously
- Add loading state
```

---

## React Errors

### "Cannot update component while rendering different component"

**What it means:**
State update during render.

**Common causes:**
- setState in render function
- setState in useEffect without deps
- Prop function calls setState

**Fix:**
```
Move state updates:
- Into useEffect
- Into event handlers
- Add dependency array
- Don't call during render
```

### "Too many re-renders"

**What it means:**
Infinite render loop.

**Common causes:**
- setState in render
- useEffect missing dependencies
- Function recreated every render

**Fix:**
```
Break the loop:
- Add useEffect dependency array
- Use useCallback for functions
- Don't setState in render
- Check infinite loops
```

### "A component is changing uncontrolled input to controlled"

**What it means:**
Input value switching between undefined and defined.

**Common causes:**
- Initial value is undefined
- Switching between null and string
- Conditional value attribute

**Fix:**
```
Always provide value:
- Default to empty string: value={data || ""}
- Don't switch between value and no value
- Initialize state properly
```

---

## Database Errors

### "Connection timeout"

**What it means:**
Can't connect to database.

**Common causes:**
- Database down
- Wrong connection string
- Network issue
- Firewall blocking

**Fix:**
```
Check connection:
- Verify database running
- Check connection string
- Check network access
- Increase timeout if needed
```

### "Deadlock detected"

**What it means:**
Two operations waiting on each other.

**Common causes:**
- Concurrent updates
- Transaction lock issues
- Complex queries

**Fix:**
```
Prevent deadlocks:
- Retry failed queries
- Simplify transactions
- Lock in consistent order
- Reduce transaction time
```

### "Duplicate entry" / "Unique constraint violation"

**What it means:**
Trying to insert duplicate unique value.

**Common causes:**
- Email already exists
- Username taken
- ID collision
- Double-submit

**Fix:**
```
Handle gracefully:
- Check existence before insert
- Catch error and show message
- Use UPDATE instead of INSERT
- Prevent double-submit
```

---

## Authentication Errors

### "Invalid token" / "Token expired"

**What it means:**
JWT token is invalid or old.

**Common causes:**
- Session expired
- Token manually modified
- Server secret changed
- Clock skew

**Fix:**
```
Handle token issues:
- Redirect to login
- Clear invalid token
- Refresh token if possible
- Show clear message
```

### "Password incorrect"

**What it means:**
Wrong password entered.

**Common causes:**
- User typo
- Caps lock on
- Wrong account
- Password changed

**Fix:**
```
Help user:
- Show "Invalid email or password"
- Don't specify which is wrong
- Add "Forgot password" link
- Limit attempts
```

---

## Payment Errors

### "Card declined"

**What it means:**
Payment method rejected.

**Common causes:**
- Insufficient funds
- Card expired
- Card blocked
- Wrong card details

**Fix:**
```
Guide user:
- Show clear error from Stripe
- Suggest trying different card
- Don't store card details
- Log for support
```

### "Payment method required"

**What it means:**
No payment method attached.

**Common causes:**
- Card not added
- Card expired
- Card removed
- Setup incomplete

**Fix:**
```
Fix workflow:
- Prompt to add card
- Guide through setup
- Verify card before checkout
- Show clear instructions
```

---

## Browser Errors

### "Not enough memory"

**What it means:**
Page using too much RAM.

**Common causes:**
- Memory leak
- Too much data loaded
- Large images
- Not cleaning up

**Fix:**
```
Reduce memory:
- Paginate data
- Lazy load images
- Clean up event listeners
- Optimize bundle size
```

### "Script error"

**What it means:**
Generic error from CDN/external script.

**Common causes:**
- CORS blocking details
- Third-party script error
- Ad blocker interference

**Fix:**
```
Limited options:
- Can't see full error
- Check third-party status
- Add fallback
- Handle gracefully
```

---

## Quick Error Diagnosis

**When you see an error:**

```
1. Read the full message
2. Note the file and line number
3. Check stack trace
4. Google if unclear
5. Give to AI with context
```

**Error template for AI:**
```
Error: [Paste full error]
Stack trace: [Paste if available]
When: [What triggers it]
Browser: [Which one]

What does this mean and how do I fix it?
```